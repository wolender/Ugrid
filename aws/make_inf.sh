#!/bin/bash

# Write one or several bash scripts (using AWS CLI) which:
# Create VPC, Subnet, Elastic Container Registry (ECR), EC2 instance, public IP address for EC2 instance, Security Groups
# Push a java spring-petlinic container image you built in “Docker” module to ECR
# ECR should be private
# Install Docker on the VM
# Run container on the VM
# Verify that application is accessible in your browser
# Remove resources

# Step 1: Create a VPC
owner_tag="wolender"
aws_region="eu-central-1"
project_tag="2023_internship_warsaw"
my_ip="0.0.0.0/0"
ami="ami-07ce6ac5ac8a0ee6f"
vpc_id=$(aws ec2 describe-vpcs --filters "Name=tag:Name,Values=vpc_wolender" --query 'Vpcs[0].VpcId' --output text)

if [[ $vpc_id == "None" ]]; then
    echo "creating vpc..."
    vpc_id=$(aws ec2 create-vpc --cidr-block 10.0.0.0/16 --query 'Vpc.VpcId' --output text --tag-specifications 'ResourceType=vpc, Tags= [{Key=Name,Value=vpc_wolender},{Key=Project,Value=2023_internship_warsaw},{Key=Owner,Value=wolender}]' )
    aws ec2 wait vpc-exists \
    --vpc-ids $vpc_id
else
    echo "vpc exists"
fi
echo "Vpc ID: $vpc_id"
subnet_id=$(aws ec2 describe-subnets --filters "Name=tag:Name,Values=sb_wolender" --query 'Subnets[*].SubnetId' --output text)
if [[ $subnet_id == "" ]]; then
    echo "creating subnet..."
    subnet_id=$(aws ec2 create-subnet --vpc-id $vpc_id --cidr-block 10.0.0.0/24 --query 'Subnet.SubnetId' --output text --tag-specifications 'ResourceType=subnet, Tags= [{Key=Name,Value=sb_wolender},{Key=Project,Value=2023_internship_warsaw},{Key=Owner,Value=wolender}]')
else
    echo "subnet exists"
fi
#creating internet gateway
gate_id=$(aws ec2 describe-internet-gateways --filters "Name=tag:Name,Values=gate_wolender" --query 'InternetGateways[0].InternetGatewayId' --output text)
if [[ $gate_id == "None" ]]; then
    echo "creating gateway..."
    gate_id=$(aws ec2 create-internet-gateway --query 'InternetGateway.InternetGatewayId' --tag-specifications 'ResourceType=internet-gateway, Tags= [{Key=Name,Value=gate_wolender},{Key=Project,Value=2023_internship_warsaw},{Key=Owner,Value=wolender}]')
else
    echo "gateway exists"
fi
#creating route table
route_id=$(aws ec2 describe-route-tables --filter "Name=tag:Name,Values=out_route_wolender" --query 'RouteTables[0].RouteTableId' --output text)
if [[ $route_id == "None" ]]; then 
    echo "creating route table..."
    route_id=$(aws ec2 create-route-table --vpc-id $vpc_id --query 'RouteTable.RouteTableId' --tag-specifications 'ResourceType=route-table, Tags= [{Key=Name,Value=out_route_wolender},{Key=Project,Value=2023_internship_warsaw},{Key=Owner,Value=wolender}]')
else
    echo "route table exists"
fi

echo "ataching gateway..."
aws ec2 attach-internet-gateway --vpc-id $vpc_id --internet-gateway-id $gate_id 2> /dev/null

aws ec2 associate-route-table --route-table-id $route_id --subnet-id $subnet_id 2> /dev/null
echo "creating routes..."
aws ec2 create-route --route-table-id $route_id --destination-cidr-block 0.0.0.0/0 --gateway-id $gate_id > /dev/null

security_group_id=$(aws ec2 describe-security-groups --filters "Name=tag:Name,Values=sg_wolender" --query 'SecurityGroups[*].GroupId' --output text)

if [[ ! $security_group_id ]]; then
    echo "creating security group..."
    security_group_id=$(aws ec2 create-security-group --group-name sg_wolender --description "Wolender Security Group" --vpc-id $vpc_id --query 'GroupId' --output text --tag-specifications 'ResourceType=security-group, Tags= [{Key=Name,Value=sg_wolender},{Key=Project,Value=2023_internship_warsaw},{Key=Owner,Value=wolender}]')
else
    echo "security group exists"
fi
echo "adding inbound traffic rules..."
aws ec2 authorize-security-group-ingress --group-id $security_group_id --protocol tcp --port 22 --cidr $my_ip 2> /dev/null
aws ec2 authorize-security-group-ingress --group-id $security_group_id --protocol tcp --port 80 --cidr "0.0.0.0/0" 2> /dev/null
aws ec2 authorize-security-group-ingress --group-id $security_group_id --protocol tcp --port 433 --cidr "0.0.0.0/0" 2> /dev/null
aws ec2 authorize-security-group-ingress --group-id $security_group_id --protocol tcp --port 8080 --cidr "0.0.0.0/0" 2> /dev/null



#creating ECR registry
ecr_name="wolender-ecr-repo"
repository_uri=$(aws ecr describe-repositories --repository-names $ecr_name --query 'repositories[*].repositoryUri' --output text 2> /dev/null)
if [[ ! $repository_uri ]]; then
    echo "creating ecr repository..."
    repository_uri=$(aws ecr create-repository --repository-name $ecr_name --query 'repository.repositoryUri' --tags Key=Environment,Value=Dev Key=Project,Value=$project_tag)
else
    echo "repository exists"
fi
echo "Repo URI $repository_uri"
#lunching instance
instance_id=$(aws ec2 describe-instances --filters "Name=tag:Name,Values=ec2_wolender" "Name=instance-state-name,Values=running" --query "Reservations[].Instances[].InstanceId" --output text)
if [[ $instance_id == "" ]]; then
    instance_id=$(aws ec2 run-instances --image-id $ami --count 1 --query 'Instances[0].InstanceId' --instance-type t2.micro --key-name wolender_key --subnet-id $subnet_id --security-group-ids $security_group_id --tag-specifications 'ResourceType=instance, Tags= [{Key=Name,Value=ec2_wolender},{Key=Project,Value=2023_internship_warsaw},{Key=Owner,Value=wolender}]' --user-data '#!/bin/bash
yum update -y
yum install -y docker
service docker start
usermod -a -G docker ec2-user
chown ec2-user:docker /var/run/docker.sock
')
else
    echo "instance exists"
fi
echo "Instance ID $instance_id"

public_address=$(aws ec2 describe-addresses --filters "Name=tag:Name,Values=ip_wolender" --query 'Addresses[0].PublicIp')
if [[ $public_address == "None" ]]; then
    echo "creating elascit ip address..."
    public_address=$(aws ec2 allocate-address --domain $vpc_id --query PublicIp --tag-specifications 'ResourceType=elastic-ip, Tags= [{Key=Name,Value=ip_wolender},{Key=Project,Value=2023_internship_warsaw},{Key=Owner,Value=wolender}]')
else
    public_address=$(aws ec2 describe-addresses --filters "Name=tag:Name,Values=ip_wolender" --query 'Addresses[0].PublicIp')
    echo "address exists"
fi
echo "Instance IP: $public_address"
instance_status=$(aws ec2 describe-instances --instance-ids $instance_id --query 'Reservations[].Instances[].State.Name' --output text)

while true; do
    instance_status=$(aws ec2 describe-instances --instance-ids $instance_id --query 'Reservations[].Instances[].State.Name' --output text)

    if [[ $instance_status == "running" ]]; then
    
        aws ec2 wait instance-running --instance-ids $instance_id
        echo "instance started, alocating arddress"
        aws ec2 associate-address --instance-id $instance_id --public-ip $public_address
        break
    else
        sleep 2
        echo "$instance_status waiting for instance to start"
    fi
done

# add role to ec2 tha enables images to be pulled allow_ec2_ecr
role="allow_ec2_ecr"
aws ec2 associate-iam-instance-profile --instance-id $instance_id --iam-instance-profile Name=$role 2>/dev/null


echo "INSTANCE IP: $public_address"
echo "INSTANCE ID: $instance_id"
echo "VPC ID: $vpc_id"
echo "SUBNET ID: $subnet_id"
echo "SEC_GROUP ID: $security_group_id"
echo "REPOSITORY URI: $repository_uri"

echo "ec2-user@$public_address" > inventory
export INSTANCE_IP=$public_address
export INSTANCE_ID=$instance_id
export REPOSITORY_URI=$repository_uri
export REPOSITORY_NAME=$ecr_name
export AWS_REGION=$aws_region

echo "========================="
echo "building app.."
echo "========================="
cd ../spring-petclinic
source ./build.sh
echo "waiting for instance os..."
sleep 60
echo "Running deployment script..."

cd ../aws
ansible-playbook playbook.yml

open http://$public_address:8080

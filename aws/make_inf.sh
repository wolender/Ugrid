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
project_tag="2023_internship_warsaw"
my_ip="78.11.118.186/32"
vpc_id=$(aws ec2 describe-vpcs --filters "Name=tag:Name,Values=vpc_wolender" --query 'Vpcs[0].VpcId')
if [[ ! $vpc_id ]]; then
    vpc_id=$(aws ec2 create-vpc --cidr-block 10.0.0.0/16 --query 'Vpc.VpcId' --output text --tag-specifications 'ResourceType=vpc, Tags= [{Key=Name,Value=vpc_wolender},{Key=Project,Value=2023_internship_warsaw},{Key=Owner,Value=wolender}]' )
else
    echo "vpc exists"
fi
subnet_id=$(aws ec2 describe-subnets --filters "Name=tag:Name,Values=sb_wolender" --query 'Subnets[*].SubnetId')
if [[ ! $subnet_id ]]; then
    subnet_id=$(aws ec2 create-subnet --vpc-id $vpc_id --cidr-block 10.0.1.0/24 --query 'Subnet.SubnetId' --output text --tag-specifications 'ResourceType=subnet, Tags= [{Key=Name,Value=sb_wolender},{Key=Project,Value=2023_internship_warsaw},{Key=Owner,Value=wolender}]')
else
    echo "subnet exists"
fi

security_group_id=$(aws ec2 describe-security-groups --filters "Name=tag:Name,Values=sg_wolender" --query 'SecurityGroups[*].GroupId' --output text)

if [[ ! $security_group_id ]]; then
    security_group_id=$(aws ec2 create-security-group --group-name sg_wolender --description "Wolender Security Group" --vpc-id $vpc_id --query 'GroupId' --output text --tag-specifications 'ResourceType=security-group, Tags= [{Key=Name,Value=sg_wolender},{Key=Project,Value=2023_internship_warsaw},{Key=Owner,Value=wolender}]')
else
    echo "security group exists"
fi

aws ec2 authorize-security-group-ingress --group-id $security_group_id --protocol tcp --port 22 --cidr $my_ip
aws ec2 authorize-security-group-ingress --group-id $security_group_id --protocol tcp --port 80 --cidr "0.0.0.0/0"
aws ec2 authorize-security-group-ingress --group-id $security_group_id --protocol tcp --port 433 --cidr "0.0.0.0/0"


echo "VPC ID: $vpc_id"
echo "SUBNET ID: $subnet_id"
echo "SEC_GROUP ID: $security_group_id"


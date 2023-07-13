#!/bin/bash

ami="ami-07ce6ac5ac8a0ee6f"
vpc_id="vpc-0211d02f52b8b8f65"
subnet_id="subnet-006b6f28a3a8b25ff"
sec_group_id="sg-04b22cbc5f61b82b1"
instance_id=$(aws ec2 describe-instances --filter "Name=tag:Name,Values=ec2_wolender" --query 'Instances[0].InstanceId')
if [[ $instance_id == "None" ]]; then
    aws ec2 run-instances --image-id $ami --count 1 --instance-type t2.micro --key-name wolender_key --subnet-id $subnet_id --security-group-ids $sec_group_id --tag-specifications 'ResourceType=instance, Tags= [{Key=Name,Value=ec2_wolender},{Key=Project,Value=2023_internship_warsaw},{Key=Owner,Value=wolender}]' --user-data '#!/bin/bash
yum update -y
yum install -y docker
service docker start
usermod -a -G docker ec2-user'
else
    echo "instance exists"
fi

public_address=$(aws ec2 describe-addresses --filters "Name=tag:Name,Values=ip_wolender" --query 'Addresses[0].PublicIp')
if [[ $public_address == "None" ]]; then
    aws ec2 allocate-address --domain $vpc_id --tag-specifications 'ResourceType=elastic-ip, Tags= [{Key=Name,Value=ip_wolender},{Key=Project,Value=2023_internship_warsaw},{Key=Owner,Value=wolender}]'
else
    echo "address exists"
fi
aws ec2 associate-address --instance-id $instance_id --public-ip $public_address

echo "$address_id"
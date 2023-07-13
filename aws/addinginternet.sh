#!/bin/bash


vpc_id="vpc-0211d02f52b8b8f65"
subnet_id="subnet-006b6f28a3a8b25ff"
gate_id=$(aws ec2 describe-internet-gateways --filters "Name=tag:Name,Values=gate_wolender" --query 'InternetGateways[0].InternetGatewayId' --output text)
if [[ $gate_id == "None" ]]; then
    aws ec2 create-internet-gateway --tag-specifications 'ResourceType=internet-gateway, Tags= [{Key=Name,Value=gate_wolender},{Key=Project,Value=2023_internship_warsaw},{Key=Owner,Value=wolender}]'
else
    echo "gateway exists"
fi

route_id=$(aws ec2 describe-route-tables --filter "Name=tag:Name,Values=out_route_wolender" --query 'RouteTables[0].RouteTableId' --output text)

if [[ $route_id == "None" ]]; then 
    route_id=$(aws ec2 create-route-table --vpc-id $vpc_id --tag-specifications 'ResourceType=route-table, Tags= [{Key=Name,Value=out_route_wolender},{Key=Project,Value=2023_internship_warsaw},{Key=Owner,Value=wolender}]')
else
    echo "route table exists"
fi

aws ec2 attach-internet-gateway --vpc-id $vpc_id --internet-gateway-id $gate_id 2> /dev/null

aws ec2 associate-route-table --route-table-id $route_id --subnet-id $subnet_id > /dev/null

aws ec2 create-route --route-table-id $route_id --destination-cidr-block 0.0.0.0/24 --gateway-id $gate_id > /dev/null

#echo "connected to $gate_id"

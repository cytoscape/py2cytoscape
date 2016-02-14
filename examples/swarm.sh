#!/bin/sh

# Get keys from standard AWS setting file location
AWS_SETTING_FILE="~/.aws/credentials"

KEY="aws_access_key_id"
SECRET="aws_secret_access_key"
aws_key=$(grep $KEY ~/.aws/credentials | cut -d "=" -f 2 | tr -d '[[:space:]]')
aws_secret=$(grep $SECRET ~/.aws/credentials | cut -d "=" -f 2 | tr -d '[[:space:]]')

#echo $aws_key
#echo $aws_secret

# Defaults
AWS_VPC="vpc-194d467b"
AWS_SECURITY_GROUP="ci-http"

AWS_PRICE="0.02"
AWS_INSTANCE_TYPE="c4.large"

aws_instance_type=$AWS_INSTANCE_TYPE
aws_price=$AWS_PRICE

help() {
    echo "Usage: $0 [-i instance-type] [-p spot-instance-price] name driver" 1>&2
    exit 1
}

while getopts i:p:h OPT
do
    case $OPT in
        i) aws_instance_type=$OPTARG
            ;;
        p) aws_price=$OPTARG
            ;;
        h) help
            ;;
        \?) help
            ;;
    esac
done

shift $((OPTIND - 1))

echo "Instance type: \033[31m $aws_instance_type \033[0m"
echo "Max. bid price: $aws_price"
echo "Machine name: \033[31m $1 \033[0m"

# Run AWS
echo "\n<Creating new Docker host: $1>\n"

# Default: Local
create() {
    echo "\nDriver:\033[31m Amazon EC2 \033[0m \n"
    # Create new host on AWS EC2
    docker-machine create --driver amazonec2 \
        --amazonec2-request-spot-instance \
        --amazonec2-access-key $aws_key \
        --amazonec2-secret-key $aws_secret \
        --amazonec2-vpc-id $AWS_VPC \
        --amazonec2-region us-west-2 \
        --amazonec2-zone b \
        --amazonec2-root-size 10 \
        --amazonec2-security-group $AWS_SECURITY_GROUP \
        --amazonec2-spot-price $aws_price --amazonec2-instance-type $aws_instance_type $1
        #--amazonec2-ami: The AMI ID of the instance to use Default: ami-4ae27e22
        #--amazonec2-iam-instance-profile: The AWS IAM role name to be used as the inst ance profile
        #--amazonec2-session-token: Your session token for the Amazon Web Services API.
        #--amazonec2-subnet-id: AWS VPC subnet id
}

create_master() {
    echo "\nCreating:\033[31m Node \033[0m \n"
    # Create new host on AWS EC2
    docker-machine create --driver amazonec2 \
        --amazonec2-request-spot-instance \
        --amazonec2-access-key $aws_key \
        --amazonec2-secret-key $aws_secret \
        --amazonec2-vpc-id $AWS_VPC \
        --amazonec2-region us-west-2 \
        --amazonec2-zone b \
        --amazonec2-root-size 10 \
        --amazonec2-security-group $AWS_SECURITY_GROUP \
        --amazonec2-spot-price $aws_price \
        --amazonec2-instance-type $aws_instance_type \
        --swarm \
        --swarm-master \
        --swarm-discovery token://$1 $2
        #--amazonec2-ami: The AMI ID of the instance to use Default: ami-4ae27e22
        #--amazonec2-iam-instance-profile: The AWS IAM role name to be used as the inst ance profile
        #--amazonec2-session-token: Your session token for the Amazon Web Services API.
        #--amazonec2-subnet-id: AWS VPC subnet id
}

create_node() {
    echo "\nCreating:\033[31m Node \033[0m \n"
    # Create new host on AWS EC2
    docker-machine create --driver amazonec2 \
        --amazonec2-request-spot-instance \
        --amazonec2-access-key $aws_key \
        --amazonec2-secret-key $aws_secret \
        --amazonec2-vpc-id $AWS_VPC \
        --amazonec2-region us-west-2 \
        --amazonec2-zone b \
        --amazonec2-root-size 10 \
        --amazonec2-security-group $AWS_SECURITY_GROUP \
        --amazonec2-spot-price $aws_price \
        --amazonec2-instance-type $aws_instance_type \
        --swarm \
        --swarm-discovery token://$1 $2
        #--amazonec2-ami: The AMI ID of the instance to use Default: ami-4ae27e22
        #--amazonec2-iam-instance-profile: The AWS IAM role name to be used as the inst ance profile
        #--amazonec2-session-token: Your session token for the Amazon Web Services API.
        #--amazonec2-subnet-id: AWS VPC subnet id
}

active_machine=$(docker-machine active)

if [ "$1" == "$active_machine" ]; then
    echo "Already active: $1\n"
else
    create $1
fi

new_machine_ip=$(docker-machine ip $1)

docker-machine ls

echo "\nNew Docker host is available at \033[31m $new_machine_ip \033[0m \n"

eval "$(docker-machine env $1)"

token=$(docker run swarm create)

echo "Token is $token"

create_node $token "swarm-node1"
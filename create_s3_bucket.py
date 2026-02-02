#!/usr/bin/env python3
"""Create S3 bucket using boto3 with the provided configuration."""

import json
import boto3
from botocore.exceptions import ClientError

# Configuration
config = {
    'key': 'CHANGE_ME',
    'secret': 'CHANGE_ME',
    'client_kwargs': {'endpoint_url': 'http://localhost:9000/'},
    'config_kwargs': {
        's3': {'addressing_style': 'path'},
        'signature_version': 's3v4'
    }
}

# Create boto3 S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=config['key'],
    aws_secret_access_key=config['secret'],
    endpoint_url=config['client_kwargs']['endpoint_url'],
    config=boto3.session.Config(
        s3=config['config_kwargs']['s3'],
        signature_version=config['config_kwargs']['signature_version']
    )
)

# Bucket name
bucket_name = 'default'

# Public read policy
public_read_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": ["s3:GetObject"],
            "Resource": [f"arn:aws:s3:::{bucket_name}/*"]
        }
    ]
}

try:
    # Check if bucket already exists
    s3_client.head_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' already exists")
    bucket_exists = True
except ClientError as e:
    error_code = e.response['Error']['Code']
    if error_code == '404':
        # Bucket doesn't exist, create it
        try:
            s3_client.create_bucket(Bucket=bucket_name)
            print(f"Successfully created bucket '{bucket_name}'")
            bucket_exists = True
        except ClientError as create_error:
            print(f"Error creating bucket: {create_error}")
            bucket_exists = False
    else:
        print(f"Error checking bucket: {e}")
        bucket_exists = False

# Apply public read policy to the bucket
if bucket_exists:
    try:
        s3_client.put_bucket_policy(
            Bucket=bucket_name,
            Policy=json.dumps(public_read_policy)
        )
        print(f"Successfully applied public read policy to bucket '{bucket_name}'")
    except ClientError as policy_error:
        print(f"Error applying bucket policy: {policy_error}")

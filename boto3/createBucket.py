import logging
import boto3
from botocore.exceptions import ClientError

# Create an Amazon S3 bucket
#
# :param bucket_name: Unique string name
# :return: True if bucket is created, else False
#

def create_bucket(bucket_name):

    s3 = boto3.client('s3')

    try:
        s3.create_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
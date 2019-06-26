import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

# how can I call create_bucket(my-bucket) here???

data = open('KennyMcCormick.png', 'rb')
s3.Bucket('my-bucket').put_object(Key='KennyMcCormick.png', Body=data)
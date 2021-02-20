import boto3

def upload_model(model_path='', s3_bucket='', key_prefix='', aws_profile='default'):
    s3 = boto3.session.Session(profile_name=aws_profile)
    client = s3.client('s3')
    client.upload_file(model_path, s3_bucket, key_prefix)


s3_bucket = 'my-nltk-layer'
model_path = './layers/nltk_lambda.zip'
key_prefix = 'nltk_lambda.zip'
upload_model(model_path, s3_bucket, key_prefix)
import boto3
import os
import base64
import json

with open('config.json') as config_file:
    data = json.load(config_file)

s3 = boto3.resource('s3', endpoint_url=data['endpoint_url'],
                    aws_access_key_id=data['aws_access_key_id'],
                    aws_secret_access_key=data['aws_secret_access_key'])

if not os.path.exists('models'):
    os.makedirs('models')
os.chdir('models/')

my_bucket = s3.Bucket(
    data['bucketName'])
my_bucket.download_file('iris_trained_model.pkl', 'iris_trained_model.pkl')

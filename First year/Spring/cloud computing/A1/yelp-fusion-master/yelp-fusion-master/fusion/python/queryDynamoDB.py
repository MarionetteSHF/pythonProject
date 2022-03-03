import json
import boto3
from boto3.dynamodb.conditions import Key

import logging
from botocore.exceptions import ClientError


import requests

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('StoredRecommendation')



thisItem = {'phone': '6462364474', 'message':'this is suggestion'}
with table.batch_writer() as batch:
    batch.put_item(Item=thisItem)

resp = table.query(KeyConditionExpression=Key('phone').eq('6462364474'))
if resp['Items']:
    print(resp['Items'])

else:
    print("no match")
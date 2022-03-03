import heapq

import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('StoredRecommendations')


response = table.query(KeyConditionExpression=Key('cuisine').eq('Seafood')&Key('phone').eq('180213587064'))

if len(response['Items']) == 0:
    print('no record with this phone number')

else:
    print(response['Items'])

nums=[1,8,2,23,7,-4,18,23,42,37,2]

print( heapq.nlargest(10, nums))
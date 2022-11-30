import json
import boto3
import os
from boto3.dynamodb.conditions import Key

table_name = os.environ["DYNAMODB_TABLE_NAME"]
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def handler(event, context):
    id = event["pathParameters"]['id']
    res = table.query(
        KeyConditionExpression=Key('id').eq(id)
    )
    todo = res["Items"][0]
    
    # body = {
    #     "message": "Go Serverless v3.0! Your function executed successfully!",
    #     "input": event,
    # }

    response = {"statusCode": 200, "body": json.dumps(todo)}

    return response
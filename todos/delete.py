import json
import boto3
import os

table_name = os.environ["DYNAMODB_TABLE_NAME"]
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def handler(event, context):
    id = event['pathParameters']['id']

    table.delete_item(
        Key={
            'id': id
        }
    )

    return {"statusCode": 204}

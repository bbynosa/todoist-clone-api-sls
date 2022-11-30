import json
import boto3
import os

table_name = os.environ["DYNAMODB_TABLE_NAME"]
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def handler(event, context):
    req = json.loads(event['body'])

    table.put_item(
        Item={
            'id': req['id'],
            'name': req['name'],
            'created_by': req['created_by'],
            'assigned_to': req['assigned_to']
        }
    )

    return {"statusCode": 201}

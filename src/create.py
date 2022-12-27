import json
import boto3
import os

table_name = os.environ["DYNAMODB_TABLE_NAME"]
dynamodb_endpoint = os.environ["DYNAMODB_SERVICE_ENDPOINT"]
dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_endpoint)
table = dynamodb.Table(table_name)


def handler(event, context):
    req = json.loads(event['body'])

    table.put_item(
        Item={
            'id': req['id'],
            'name': req['name'],
            'status': req['status'],
            'priority': req['priority'],
            'notes': req['notes'],
            'created_by': req['created_by'],
            'assigned_to': req['assigned_to']
        }
    )

    return {"statusCode": 201,
            "headers": {
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "*"
            }, }

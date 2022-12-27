import json
import boto3
import os

table_name = os.environ["DYNAMODB_TABLE_NAME"]
dynamodb_endpoint = os.environ["DYNAMODB_SERVICE_ENDPOINT"]
dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_endpoint)
table = dynamodb.Table(table_name)


def handler(event, context):
    id = event['pathParameters']['id']

    table.delete_item(
        Key={
            'id': id
        }
    )

    return {"statusCode": 204,
            "headers": {
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "*"
            }, }

import json
import boto3
import os

table_name = os.environ["DYNAMODB_TABLE_NAME"]
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def handler(event, context):
    res = table.scan()
    todos = res["Items"]

    response = {"statusCode": 200, "body": json.dumps(todos)}

    return response
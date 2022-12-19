import json
import boto3
import os
from boto3.dynamodb.conditions import Key

table_name = os.environ["DYNAMODB_TABLE_NAME"]
dynamodb_endpoint = os.environ["DYNAMODB_SERVICE_ENDPOINT"]
dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_endpoint)
table = dynamodb.Table(table_name)


def handler(event, context):
    # id = event["pathParameters"]['id']
    # res = table.query(
    #     KeyConditionExpression=Key('id').eq(id)
    # )
    # todo = res["Items"][0]

    # response = {"statusCode": 200, "headers": {
    #     "Access-Control-Allow-Headers": "*",
    #     "Access-Control-Allow-Origin": "*",
    #     "Access-Control-Allow-Methods": "*"
    # }, "body": json.dumps(todo)}

    response = {"statusCode": 200, "headers": {
        "Access-Control-Allow-Headers": "*",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "*"
    }, "body": json.dumps("Hello sls pipelines!")}

    return response

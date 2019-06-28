import os
import boto3
import json

STOCK_TABLE = os.environ['STOCK_TABLE']
client = boto3.client('dynamodb')

def save(event, context):
    data = json.loads(event['body'])

    if ('sku' not in data) or ('stock' not in data):
        response = {
            "statusCode": 401,
            "body": json.dumps({"message": "Params not found"})
        }

        return response
        
    sku = data['sku']
    stock = data['stock']

    resp = client.put_item(
        TableName=STOCK_TABLE,
        Item={
            'sku': {'S': sku },
            'stock': {'S': stock }
        }
    )

    response = {
        "statusCode": 200,
        "body": json.dumps({"Message": "Item updated successfully"})
    }

    return response
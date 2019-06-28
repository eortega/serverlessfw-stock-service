import os
import json



def handle(event, context):
    sku = event['pathParameters']['sku']
    table = dynamodb.Table(os.environ['STOCK_TABLE'])

    resp = table.get_item(
        Key={
            'sku': sku
        }
    )

    item = resp.get('Item')
    if not item:
        response = {
            "statusCode": 404,
            "body": json.dumps({"Message":"Item not found"})
        }

        return response
        
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
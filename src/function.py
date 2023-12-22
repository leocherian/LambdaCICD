import os
import json

env = os.environ['ENV']
def lambdaHandler(event, context):
    message = 'Hello from '+env
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }

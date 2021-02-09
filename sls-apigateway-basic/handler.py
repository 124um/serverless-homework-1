import json

def hello(event, context):
    if(event["queryStringParameters"] is None ):
        message = "HELLO WORLD" 
    else:        
        message = "Hello " + event["queryStringParameters"]["name"]

    body = {
        "message": message,
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def moc(event, context):

    response = {
        "statusCode": 200,
        "body": "Hello! My name is " + json.dumps(event.get('pathParameters', {}))
    }

    return response

def hola(event, context):

    body = event.get('body', {})

    response = {
        "statusCode": 200,
        "body": json.dumps({ 
            "message": body,
            "input": event
        })
    }

    return response    
from conf import *
from search import *

import json

print('Loading serverless function.')


def verifyParameters(parameters):
    """ returns whether the event contains the required parameters """
    return (set(required_keys_list).issubset(parameters.keys()))


def createReturnObject(body="", code=200):
    """ create a dictionary object to return the result"""

    return {
        'statusCode': code,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(body)
    }


def lambda_handler(event, context):
    parameters = event["queryStringParameters"]

    if (not verifyParameters(parameters)):
        return createReturnObject("InvalidParameter Error")

    return createReturnObject("REST API Test Success")




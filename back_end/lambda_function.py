from conf import *
from search import findNews
from agent import mediaPool

import json

print('Loading serverless function.')


def _extractDomain(url):
    # type: (str) -> str
    url = url.replace("https://", "")
    url = url.replace("http://", "")
    url = url.replace("www.", "")
    if "/" in url:
        url = url[:url.index("/")]
    return url


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


def getBalancedNews(url, title):
    responseBody = {
        "success": 0
    }

    media, success = mediaPool.findMediaWithUrl(url)
    if not success:
        return responseBody
    else:
        responseBody["success"] = 1

    responseBody["currentMedia"] = {
        "name": media.getName(),
        "partisanScore": media.getPartisanScore()

    }

    balancedMedia = mediaPool.findClosestMediawithPartisanScore(-media.getPartisanScore())
    responseBody["balancedMedia"] = {
        "name": balancedMedia.getName(),
        "partisanScore": balancedMedia.getPartisanScore()
    }

    balancedNewsContent = findNews(source=balancedMedia.getUrl(), title=title)
    responseBody["balancedNews"] = balancedNewsContent

    return responseBody


def lambda_handler(event, context):
    parameters = event["queryStringParameters"]

    if (not verifyParameters(parameters)):
        return createReturnObject("InvalidParameter Error")

    title = parameters["news_title"]
    url = _extractDomain(parameters["news_source"])

    body = getBalancedNews(url=url, title=title)

    return createReturnObject(body)




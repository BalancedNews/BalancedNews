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
    # type: (list) -> bool
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
    """get the opposite side news' name, url, and title by given current news url and title"""
    responseBody = {
        "success": 0
    }

    media, success = mediaPool.findMediaWithUrl(url)
    if not success:
        return responseBody
    else:
        responseBody["success"] = 1

    balancedMedia = mediaPool.findClosestMediawithPartisanScore(-media.getPartisanScore())
    responseBody["name"] = balancedMedia.getName()
    responseBody["partisanScore"] = balancedMedia.getPartisanScore()
    balancedNewsContent = findNews(source=balancedMedia.getUrl(), title=title)
    responseBody["content"] = balancedNewsContent

    return responseBody


def rateCurrentNews(url):
    """get the name and partisan score for the current news channel"""
    responseBody = {
        "success": 0
    }

    media, success = mediaPool.findMediaWithUrl(url)
    if not success:
        return responseBody
    else:
        responseBody["success"] = 1

    responseBody["name"] = media.getName()
    responseBody["partisanScore"] = media.getPartisanScore()

    return responseBody

# Event handler for AWS Serverless function
def lambda_handler(event, context):
    # verify the parameters first
    parameters = event["queryStringParameters"]
    if (not verifyParameters(parameters)):
        return createReturnObject("InvalidParameter Error")

    # extract each parameter with a variable
    title = parameters["news_title"]
    url = _extractDomain(parameters["news_source"])
    api = parameters["api"]

    # the "api" parameter decides which function to call
    if api == "getBalancedNews":
        body = getBalancedNews(url=url, title=title)
    elif api == "rateCurrentNews": 
        body = rateCurrentNews(url=url)
    else: # if there is no matching function, return an error
        return createReturnObject("InvalidParameter Error")

    # insert the results into a response object before returning
    return createReturnObject(body)




from googleapiclient.discovery import build

from utils import constants
from utils.google import snippetModifier


def getAnswerJsonFunc(question):
    resource = build("customsearch", 'v1', developerKey=constants.google_search_api_key).cse()

    result = resource.list(q=question, cx='d386675b7aefdab59').execute()

    responseJson = result['items']

    return responseJson


def getOnlyRelevantInReceivedJson(receivedJson, relevantIndexesArr):

    returnArr = []

    for indexItem in relevantIndexesArr:
        for index, jsonItem in enumerate(receivedJson):
            if index == indexItem['i']:
                returnArr.append(jsonItem)

    return returnArr


def setAnswersFromFormattedJson(formattedJson):
    answers = []
    for formattedJsonItem in formattedJson:

        if 'snippet' in formattedJsonItem != True:
            formatted_snip = snippetModifier.snippetModifierFunc(formattedJsonItem['snippet'])
            answers.append({"a": formatted_snip, "cited": formattedJsonItem['link']})
    return answers

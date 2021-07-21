import pickle
import re

import nltk

from model.Videoquestion import Videoquestion
from model.chatquestion import Chatquestion
from utils import constants


def domainNonDomainQuestionClassifierFunc(question_arr, mode):
    f = open('tempStorage/trainedData/domain_related_or_not_classifier_1.pickle', 'rb')
    classifier = pickle.load(f)
    f.close()

    f = open('tempStorage/trainedData/domain_related_or_not_classifier_2.pickle', 'rb')
    classifier2 = pickle.load(f)
    f.close()

    if mode == 'Chat':
        filteredChatQuestionTempArr = []
        for questionItem in question_arr:
            stripped_line = questionItem.question.strip()
            type = classifier.classify(dialogue_act_features(stripped_line));
            qtype = classifier2.classify(dialogue_act_features(stripped_line));
            if qtype == 'Domain':
                questionItem.question = cleanquestionText(questionItem.question)
                newFilteredChatQuestionObj = Chatquestion(questionItem.timestamp, questionItem.sender,
                                                          questionItem.receiver, questionItem.question,
                                                          questionItem.question_type, False, "", [])
                filteredChatQuestionTempArr.append(newFilteredChatQuestionObj)
        constants.chat_file_question_arr = filteredChatQuestionTempArr
    elif mode == 'Video':
        filteredVideoQuestionTempArr = []
        for questionItem in question_arr:
            stripped_line = questionItem.question.strip()
            type = classifier.classify(dialogue_act_features(stripped_line));
            qtype = classifier2.classify(dialogue_act_features(stripped_line));
            if qtype == 'Domain':
                questionItem.question = cleanquestionText(questionItem.question)
                newFilteredVideoQuestionObj = Videoquestion(questionItem.startTime, questionItem.endTime,
                                                            questionItem.speakerType, questionItem.question,
                                                            questionItem.sentence_type, False, "", [], False, "")
                filteredVideoQuestionTempArr.append(newFilteredVideoQuestionObj)
        constants.video_file_question_arr = filteredVideoQuestionTempArr


def dialogue_act_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains({})'.format(word.lower())] = True
    return features


def cleanquestionText(questionText):
    questionText = re.sub("(?i)sir", "", questionText)
    questionText = re.sub("(?i)madam", "", questionText)
    questionText = re.sub("(?i)sir,", "", questionText)
    questionText = re.sub("(?i)madam,", "", questionText)
    questionText = re.sub("(?i),", "", questionText)

    return questionText

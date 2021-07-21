import nltk

from model.Videoquestion import Videoquestion
from model.chatquestion import Chatquestion
from utils import constants

nltk.download('nps_chat')
posts = nltk.corpus.nps_chat.xml_posts()[:10000]


def identify_interrogative_or_not(Arr, mode):
    featuresets = [(dialogue_act_features(post.text), post.get('class')) for post in posts]
    size = int(len(featuresets) * 0.1)
    train_set, test_set = featuresets[size:], featuresets[:size]
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    if mode == "Chat":
        tempArr = []
        for charArrItem in Arr:
            sentence = charArrItem['msg']
            sentence_type = classifier.classify(dialogue_act_features(sentence))

            timestamp = charArrItem['timestamp']
            sender = charArrItem['from']
            receiver = charArrItem['to']

            if sentence_type.find('Question') >= 0:
                question = charArrItem['msg']
                newChatQuestionObj = Chatquestion(timestamp,sender,receiver,question,sentence_type, False,"",[])
                tempArr.append(newChatQuestionObj)

        constants.chat_file_question_arr = tempArr
    elif mode == "Video":
        tempArr = []
        for arrItem in Arr:
            sentenceStr = arrItem.get_sentenceStr()
            startTime = arrItem.get_sentenceStartTime()
            endTime = arrItem.get_sentenceEndTime()
            speakerType = arrItem.get_sentenceSpeakerType()

            sentence_type = classifier.classify(dialogue_act_features(sentenceStr))

            if sentence_type.find('Question') >= 0:
                question = sentenceStr
                newVideoQuestionObj = Videoquestion(startTime, endTime, speakerType, question, sentence_type, False, "", [], False,"")
                tempArr.append(newVideoQuestionObj)

            constants.video_file_question_arr = tempArr
    return True


def dialogue_act_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains({})'.format(word.lower())] = True
    return features

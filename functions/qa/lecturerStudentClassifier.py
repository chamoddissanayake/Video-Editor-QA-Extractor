import pickle

import nltk

import utils
from model.sentence import Sentence
from model.speaker import Speaker
from utils.constants import all_sentences_obj_arr


def getSpeakerCountObj(map, key):
    if (key in map):
        return map[key]
    return Speaker()


def lecturerStudentClassifierFunc(all_sentences_obj_arr):

    def dialogue_act_features(post):
        features = {}
        for word in nltk.word_tokenize(post):
            features['contains({})'.format(word.lower())] = True
        return features

    f = open('tempStorage/trainedData/lecturer_student_classifier_1.pickle', 'rb')
    classifier = pickle.load(f)
    f.close()

    f = open('tempStorage/trainedData/lecturer_student_classifier_2.pickle', 'rb')
    classifier2 = pickle.load(f)
    f.close()

    countMap = {}

    for item in all_sentences_obj_arr:
        sentenceStr = item.get_sentenceStr()
        speakerName = item.get_sentenceSpeakerType()

        stripped_line = sentenceStr.strip()
        type = classifier.classify(dialogue_act_features(stripped_line))
        speaker_type = classifier2.classify(dialogue_act_features(stripped_line))
        instance = getSpeakerCountObj(countMap, speakerName)
        if speaker_type == 'Lecturer':
            instance.increaseLecturerCount()
        else:
            instance.increaseStudentCount()

        countMap[speakerName] = instance;

    lecturerName = ""
    lecturerSize = 0

    for item in countMap:

        if countMap[item].lecturerCount > lecturerSize:
            lecturerName = item
            lecturerSize = countMap[item].lecturerCount


    finalObjList = []

    for item in all_sentences_obj_arr:
        sentenceStr = item.get_sentenceStr()
        sentenceStartTime = item.get_sentenceStartTime()
        sentence_endTime = item.get_sentenceEndTime()
        speakerName = item.get_sentenceSpeakerType()

        if speakerName == lecturerName:
            temp_sentence = Sentence(sentenceStr, sentenceStartTime, sentence_endTime, 'Lecturer')
        else:
            temp_sentence = Sentence(sentenceStr, sentenceStartTime, sentence_endTime, 'Student')

        finalObjList.append(temp_sentence)
    utils.constants.all_sentences_obj_arr = finalObjList

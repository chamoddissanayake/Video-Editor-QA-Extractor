import pickle

import nltk

from model.Videoquestion import Videoquestion
from utils import constants


def checkIfQuestionAskedFromStudentAndLecturerProvidedAnswer():
    def dialogue_act_features(post):
        features = {}
        for word in nltk.word_tokenize(post):
            features['contains({})'.format(word.lower())] = True
        return features

    f = open('tempStorage/trainedData/answer_give_or_not_classifier_1.pickle', 'rb')
    classifier = pickle.load(f)
    f.close()

    f = open('tempStorage/trainedData/answer_give_or_not_classifier_2.pickle', 'rb')
    classifier2 = pickle.load(f)
    f.close()

    for index_q, vid_question_item in enumerate(constants.video_file_question_arr):
        if vid_question_item.speakerType == 'Student' and "question" in vid_question_item.sentence_type.lower():

            counter = 0
            for voice_q_item in constants.all_sentences_obj_arr:
                if voice_q_item.get_sentenceStr() == vid_question_item.question:
                    break
                counter += 1
            for index, voice_q_item in enumerate(constants.all_sentences_obj_arr):
                if index == counter + 1:
                    if voice_q_item.get_sentenceSpeakerType() == 'Lecturer':
                        t_answer = voice_q_item.get_sentenceStr()
                        type2 = classifier2.classify(dialogue_act_features(t_answer));

                        if type2 == 'HasAnswer':
                            newVideoQAObj = Videoquestion(
                                vid_question_item.startTime,
                                vid_question_item.endTime,
                                vid_question_item.speakerType,
                                vid_question_item.question,
                                vid_question_item.sentence_type,
                                True, t_answer, [],

                                False, "")
                        else:
                            newVideoQAObj = Videoquestion(
                                vid_question_item.startTime,
                                vid_question_item.endTime,
                                vid_question_item.speakerType,
                                vid_question_item.question,
                                vid_question_item.sentence_type,
                                False, "", [],
                                False, "")

                        constants.video_file_question_arr[index_q] = newVideoQAObj

    return True

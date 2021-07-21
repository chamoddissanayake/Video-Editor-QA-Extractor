import pickle

import nltk
from fuzzywuzzy import fuzz

from model.chatquestion import Chatquestion
from model.sentence import Sentence
from utils import constants
from utils import tags


def checkWhetherLecturersGivenStatementIsAValidAnswer(answerFromLecturer):
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

    type2 = classifier2.classify(dialogue_act_features(answerFromLecturer));
    if type2 == 'HasAnswer':
        return True
    else:
        return False


def findChatAnswersInVideoFunc():

    temp_all_sentences_obj_arr = []
    for sentence_item in constants.all_sentences_obj_arr:
        sentence_str = sentence_item.get_sentenceStr()
        sentence_start_time = sentence_item.get_sentenceStartTime()
        sentence_endTime = sentence_item.get_sentenceEndTime()
        speaker_name = sentence_item.get_sentenceSpeakerType()

        for a in tags.removetags:
            sentence_str = ireplace(a, "", sentence_str)

        temp_sentence = Sentence(sentence_str, sentence_start_time, sentence_endTime, speaker_name)

        temp_all_sentences_obj_arr.append(temp_sentence)

    allSentencesLoopCount = 0

    for sentence_item in temp_all_sentences_obj_arr:
        sentence_str = sentence_item.get_sentenceStr()
        for index, chat_question_item in enumerate(constants.chat_file_question_arr):
            q_from_chat = chat_question_item.question

            ratio = fuzz.ratio(q_from_chat, sentence_str)
            if ratio > constants.fuzzRatioCutPoint:
                for idx, val in enumerate(temp_all_sentences_obj_arr):

                    if idx == allSentencesLoopCount + 1:
                        answerFromLecturer = val.get_sentenceStr()
                        isValidAnswer = checkWhetherLecturersGivenStatementIsAValidAnswer(answerFromLecturer)

                        if isValidAnswer:
                            newUpdatedChatQuestionObj = Chatquestion(
                                constants.chat_file_question_arr[index].timestamp,
                                constants.chat_file_question_arr[index].sender,
                                constants.chat_file_question_arr[index].receiver,
                                constants.chat_file_question_arr[index].question,
                                constants.chat_file_question_arr[index].question_type,
                                True,
                                answerFromLecturer,
                                constants.chat_file_question_arr[index].google_answer
                            )
                            constants.chat_file_question_arr[index] = newUpdatedChatQuestionObj
                        else:
                            newUpdatedChatQuestionObj = Chatquestion(
                                constants.chat_file_question_arr[index].timestamp,
                                constants.chat_file_question_arr[index].sender,
                                constants.chat_file_question_arr[index].receiver,
                                constants.chat_file_question_arr[index].question,
                                constants.chat_file_question_arr[index].question_type,
                                False,
                                "",
                                constants.chat_file_question_arr[index].google_answer
                            )
                            constants.chat_file_question_arr[index] = newUpdatedChatQuestionObj

                        break
                break

        allSentencesLoopCount += 1


def ireplace(old, new, text):
    idx = 0
    while idx < len(text):
        index_l = text.lower().find(old.lower(), idx)
        if index_l == -1:
            return text
        text = text[:index_l] + new + text[index_l + len(old):]
        idx = index_l + len(new)
    return text

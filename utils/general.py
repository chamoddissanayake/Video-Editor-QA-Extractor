import os
import re
import sys

from model.Videoquestion import Videoquestion
from model.sentence import Sentence
from utils import constants
from utils import tags


def appRestart():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def getSplittedSentece(sentence):
    str = ""
    splitted_sentence = sentence.split(' ')

    counter = 1
    for aaa in splitted_sentence:
        str = str + aaa + " "
        if counter % 15 == 0:
            str = str.strip() + "\n"
        counter += 1

    return str


def removeUnwantedPartsInText_video_file_question_arr():
    for i, item in enumerate(constants.video_file_question_arr):
        que = item.question
        for a in tags.removetags:
            pattern = re.compile(a, re.IGNORECASE)
            que = pattern.sub("", que)

        constants.video_file_question_arr[i].question = que


def removeUnwantedPartsInText_all_sentences_obj_arr():

    for i, sentence_item in enumerate(constants.all_sentences_obj_arr):
        sentence_str = sentence_item.get_sentenceStr()
        sentence_start_time = sentence_item.get_sentenceStartTime()
        sentence_endTime = sentence_item.get_sentenceEndTime()
        speaker_name = sentence_item.get_sentenceSpeakerType()
        sentence = sentence_str
        for a in tags.removetags:
            pattern = re.compile(a, re.IGNORECASE)
            sentence = pattern.sub("", sentence)

        temp_sentence = Sentence(sentence, sentence_start_time, sentence_endTime, speaker_name)

        constants.all_sentences_obj_arr[i] = temp_sentence


def identifyPartsInvideo_file_question_arr():
    for i, video_file_question_item in enumerate(constants.video_file_question_arr):
        question = video_file_question_item.question,

        for a in tags.removetags:
            if str(question).find(a) != -1:
                updatedQuestion = ireplace(a, "", question[0])

                newVideoQATempObj = Videoquestion(
                    video_file_question_item.startTime,
                    video_file_question_item.endTime,
                    video_file_question_item.speakerType,
                    updatedQuestion,
                    video_file_question_item.sentence_type,
                    False, "", [],
                    True, question[0])
                constants.video_file_question_arr[i] = newVideoQATempObj

    removeNoneInvideo_file_question_arr()

def ireplace(old, new, text):
    idx = 0
    while idx < len(text):
        index_l = text.lower().find(old.lower(), idx)
        if index_l == -1:
            return text
        text = text[:index_l] + new + text[index_l + len(old):]
        idx = index_l + len(new)
    return text


def removeNoneInvideo_file_question_arr():
    tempArr = []
    for i in constants.video_file_question_arr:
        if i is not None:
            tempArr.append(i)
    constants.video_file_question_arr = tempArr


def getCheckedInBool(checked_number):
    checked_number_num = int(checked_number)
    if checked_number_num == 1:
        return True
    elif checked_number_num == 0:
        return False


def sort_enable_vid_first_q_with_a_and_then_q_without_a(enable_vid):
    q_with_a_arr = []
    q_without_a_arr = []

    for item in enable_vid:
        if item['has_lecturer_answer']:
            q_with_a_arr.append(item)

    for item in enable_vid:
        if item['has_lecturer_answer'] == False:
            q_without_a_arr.append(item)
    full_arr = q_with_a_arr + q_without_a_arr
    return full_arr


def sort_enable_chat_first_q_with_a_and_then_q_without_a(enable_chat):
    q_with_a_arr = []
    q_without_a_arr = []

    for item in enable_chat:
        if item['has_lecturer_answer']:
            q_with_a_arr.append(item)

    for item in enable_chat:
        if item['has_lecturer_answer'] == False:
            q_without_a_arr.append(item)
    full_arr = q_with_a_arr + q_without_a_arr
    return full_arr

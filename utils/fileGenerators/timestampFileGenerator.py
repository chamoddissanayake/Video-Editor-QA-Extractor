import datetime
import json
import os
import tkinter.messagebox

from model.jsonobj import JSONObj
from utils import constants


def generateTimestampJson(filename):
    readyJSONObjectArr = []
    counter = 0
    for sentence_item in constants.all_sentences_obj_arr:

        sentence_str = sentence_item.get_sentenceStr()
        sentence_start_time = sentence_item.get_sentenceStartTime()
        sentence_end_time = sentence_item.get_sentenceEndTime()
        speaker_type = sentence_item.get_sentenceSpeakerType()

        newJSONObj = None
        found = False

        for question_item in constants.video_q_with_a:
            question_str = question_item['question']
            question_start_time = question_item['startTime']
            question_end_time = question_item['endTime']
            q_speaker_type = question_item['speakerType']
            q_lecturer_answer = question_item['lecturer_answer']
            q_has_lecturer_answer = question_item['has_lecturer_answer']

            for item in constants.video_q_with_a:
                if question_str.strip() == item['question'].strip():
                    google_ans = item['google_answer']
                    break

            if sentence_start_time == question_start_time and sentence_end_time == question_end_time:
                google_answer = google_ans

                newJSONObj = JSONObj(counter + 1, question_start_time, question_end_time, q_speaker_type, True,
                                     google_answer, q_lecturer_answer, q_has_lecturer_answer, question_str)
                readyJSONObjectArr.append(newJSONObj)
                found = True
                break
            else:
                found = False
        if not found:
            newJSONObj = JSONObj(counter + 1, sentence_start_time, sentence_end_time, speaker_type, False, [], "",
                                 False, sentence_str)
            readyJSONObjectArr.append(newJSONObj)

    json_string = ""
    jsArr = [];
    if len(readyJSONObjectArr) > 0:
        json_string += "["

        loopcount = 1

        for item in readyJSONObjectArr:
            start_timestamp_in_hh_mm_ss = datetime.timedelta(seconds=int(item.start_timestamp))

            temp = {'index': loopcount,
                    'start_timestamp': str(start_timestamp_in_hh_mm_ss),
                    'end_timestamp': str(datetime.timedelta(seconds=int(item.end_timestamp))),
                    'speaker': item.speaker,
                    'is_question': item.is_question,
                    'google_answer': item.google_answer,
                    'lecturer_answer': item.lecturer_answer,
                    'has_lecturer_answer': item.has_lecturer_answer,
                    'sentence_str': item.sentence_str
                    }
            jsArr.append(temp);
            loopcount += 1
        json_string += "]"

        outputtimestampFile = os.path.abspath(os.curdir) + "/tempStorage/generatedFiles/" + filename + '.json'

        with open(outputtimestampFile, 'w') as file:
            json.dump(jsArr, file)
        tkinter.messagebox.showinfo(title='success', message='Json File saved successfully')

        constants.finalSavedJsonPath = outputtimestampFile
    return True

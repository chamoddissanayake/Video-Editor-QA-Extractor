import json
from decimal import Decimal

import utils
from components.subComponents import progressWindow
from components.subComponents.transcriptWindow import fillTranscriptWindow
from functions.qa import lecturerStudentClassifier
from model.sentence import Sentence


def extractDataFromResponseJSON(savedJSONPath):
    progressWindow.status_label.config(text="Extracting data from response")

    with open(savedJSONPath) as f:
        data = json.load(f)

    segmentsArr = data['results']['speaker_labels']['segments']

    for segment in segmentsArr:
        sentence_start_time = Decimal(segment['start_time'])
        sentence_speaker = segment['speaker_label']
        sentence_end_time = Decimal(segment['end_time'])
        word_position = 0

        sentence = ""
        for segment1 in data['results']['items']:
            start_set = True
            end_set = True

            try:
                word_start_time = Decimal(segment1['start_time'])
            except:
                start_set = False

            try:
                word_end_time = Decimal(segment1['end_time'])
            except:
                end_set = False

            word_type = segment1['type']
            word_content = segment1['alternatives'][0]['content']

            if sentence_start_time <= word_start_time and sentence_end_time >= word_end_time:
                if word_type == 'punctuation':
                    sentence += word_content
                    word_position += 1
                else:
                    if word_position == 0:
                        sentence += word_content
                        word_position += 1
                    else:
                        sentence += " " + word_content
                        word_position += 1

        temp_sentence = Sentence(sentence, sentence_start_time, sentence_end_time, sentence_speaker)

        utils.constants.all_sentences_obj_arr.append(temp_sentence)
        word_position == 0

    lecturerStudentClassifier.lecturerStudentClassifierFunc(utils.constants.all_sentences_obj_arr)
    fillTranscriptWindow()

# import azure.cognitiveservices.speech as speechsdk
#
# def from_file():
#     speech_config = speechsdk.SpeechConfig(subscription="9de9f6d9f32e4ff3bf3f86e84f07aabf", region="eastus")
#     # audio_input = speechsdk.AudioConfig(filename="nuwan-sir-par-processing-30sec.wav")
#     audio_input = speechsdk.AudioConfig(filename="out.wav")
#     speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
#
#     result = speech_recognizer.recognize_once_async().get()
#
#     if result.reason == speechsdk.ResultReason.RecognizedSpeech:
#         print("Recognized: {}".format(result.text))
#     elif result.reason == speechsdk.ResultReason.NoMatch:
#         print("No speech could be recognized: {}".format(result.no_match_details))
#     elif result.reason == speechsdk.ResultReason.Canceled:
#         cancellation_details = result.cancellation_details
#         print("Speech Recognition canceled: {}".format(cancellation_details.reason))
#         if cancellation_details.reason == speechsdk.CancellationReason.Error:
#             print("Error details: {}".format(cancellation_details.error_details))
#
#     print(result.text)
#
#
# from_file()

import sys
import time
from typing import List, Any

import requests
import mutagen


class AssemblyAI_API_Error(Exception):
    """Exception raised for errors occurred with AssemblyAI API Requests.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


error_status_codes = [400, 401, 500]


def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data


api_key = "d911e588ff47453eb689cf213bb7dc83"


def file_upload(filename):
    headers = {'authorization': api_key}
    response = requests.post('https://api.assemblyai.com/v2/upload',
                             headers=headers,
                             data=read_file(filename))

    upload_url = response.json()["upload_url"]
    print(response.json())

    return upload_url


def send_audio_url_for_transcription(upload_url):
    json = {
        "audio_url": str(upload_url),
        "speaker_labels": True
    }
    headers = {
        "authorization": api_key,
        "content-type": "application/json"
    }

    endpoint = "https://api.assemblyai.com/v2/transcript"
    response = requests.post(endpoint, json=json, headers=headers)

    if response.status_code in error_status_codes:
        raise AssemblyAI_API_Error(response.json()['error'])

    print(response.json())
    transcription_id = response.json()['id']
    return transcription_id


def get_transcription_job_result(transcription_id, request_count, request_interval):
    # test_id = '8ox5zx6nb-3fe5-460e-91f0-eb17a9d6859d'
    endpoint = "https://api.assemblyai.com/v2/transcript/" + transcription_id

    headers = {
        "authorization": api_key,
    }
    try_again = True
    reqCount = 0
    returnObj = {
        'transcription_done': False,
        'transcription': '',
        'error': False
    }

    while try_again and not reqCount > request_count:
        print("inside")
        try:
            response = requests.get(endpoint, headers=headers)
            reqCount += 1
            json_response = response.json()
            print(json_response)
            if response.status_code in error_status_codes:
                raise AssemblyAI_API_Error(json_response['error'])
            elif json_response['status'] == 'completed':
                try_again = False
                returnObj['transcription_done'] = True
                returnObj['transcription'] = response.json()['text']
                returnObj['words'] = response.json()['words']
            elif json_response['status'] == 'error' and json_response['error']:
                raise AssemblyAI_API_Error(json_response['error'])
            else:
                print(response.json()['status'])
                time.sleep(request_interval)  # delaying to invoke next request
        except AssemblyAI_API_Error as assembly_api_error:
            try_again = False
            returnObj['error'] = str(assembly_api_error)

    return returnObj


def get_transcription_from_assembly_ai(path_to_audio_file):
    audio_mutagen = mutagen.File(path_to_audio_file)
    selected_audio_length = round(audio_mutagen.info.length, 2)
    print('selected_audio_length' + str(selected_audio_length))
    possible_completion_duration = round(selected_audio_length * 30 / 100, 2)
    requests_interval = 5
    required_request_count = possible_completion_duration / requests_interval + 1
    print("possible_completion_duration: " + str(possible_completion_duration))
    print("required_request_count: " + str(int(required_request_count)))
    # return

    if selected_audio_length > 0:
        upload_url = file_upload(path_to_audio_file)
        transcription_id = send_audio_url_for_transcription(upload_url)
        result = get_transcription_job_result(transcription_id, selected_audio_length, required_request_count)
        print(result['transcription'])
        return get_lecturer_transcription(result['words'])
    else:
        print('Audio file is empty')
        return


# audio_file = 'nuwan-sir-par-processing-30sec.wav'
# get_transcription_from_assembly_ai(audio_file)

def get_lecturer_transcription(words_array):
    spoke_persons = {}
    for word in words_array:
        if word["speaker"] not in spoke_persons:
            spoke_persons[word["speaker"]] = 1
        else:
            spoke_persons[word['speaker']] = spoke_persons[word['speaker']] + 1
    lecturer_type = max(spoke_persons, key=spoke_persons.get)
    lecturer_words = ''
    if len(spoke_persons) > 0:
        for word in words_array:
            if word['speaker'] == lecturer_type:
                lecturer_words += str(word['text']) + ' '

    return lecturer_words


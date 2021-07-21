from __future__ import print_function

import os
import time
import tkinter.messagebox

import boto3
import requests

import utils
from components.subComponents import progressWindow, AdPlayer
from functions.qa.responseJSONHandler import extractDataFromResponseJSON
from utils import value

global downloadable_json_url


def getTranscribedJson(notebook):
    global downloadable_json_url
    tkinter.messagebox.showinfo(title='Success', message='Transcribe is going to start.')

    utils.constants.main_player.pause()
    winShowAd = AdPlayer.showAdPopup()

    value.program_status = 'TRANSCRIBING'
    progressWindow.bar(0)
    progressWindow.status_label.config(text="Identifying text. Please wait")

    progressWindow.hide_determinate()
    progressWindow.show_indeterminate()

    transcribe = boto3.client('transcribe')
    job_name = str(int(time.time()))
    job_uri = utils.constants.uploaded_audio_s3_path
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='mp3',
        LanguageCode='en-US',
        # Type = 'CONVERSATION',
        Settings={'ShowSpeakerLabels': True,
                  'MaxSpeakerLabels': 10
                  }
    )

    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        print("Not ready yet...")
        progressWindow.barIndeterminate()
        time.sleep(0.25)
    downloadable_json_url = status["TranscriptionJob"]["Transcript"]["TranscriptFileUri"]

    AdPlayer.close(winShowAd)
    utils.constants.main_player.play()
    tkinter.messagebox.showinfo(title='Success', message='Transcribed response received')

    progressWindow.hide_indeterminate()
    progressWindow.show_determinate()

    saveTranscribedJson()
    return True


def saveTranscribedJson():
    value.program_status = 'SAVING_JSON'
    progressWindow.status_label.config(text="Saving response data")
    dir_path = os.path.dirname(os.path.realpath(__file__))

    current_dir = os.path.abspath(os.curdir) + "/tempStorage/responseJSON/"

    url = downloadable_json_url
    r = requests.get(url)

    with open(current_dir + utils.constants.current_time + '.json', 'wb') as f:
        f.write(r.content)

    tkinter.messagebox.showinfo(title='Success', message='JSON Saved successfully')

    savedJSONPath = current_dir + utils.constants.current_time + '.json'
    extractDataFromResponseJSON(savedJSONPath)
    return True
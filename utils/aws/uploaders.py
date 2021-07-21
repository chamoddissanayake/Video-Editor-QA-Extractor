import logging
import os
import sys
import threading
import tkinter.messagebox

import boto3
from botocore.exceptions import ClientError

import utils
from components.subComponents import progressWindow
from utils import value
from utils.aws.transcribe import getTranscribedJson


class ProgressPercentage(object):

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write("\r%s  %s / %s  (%.2f%%)" % (self._filename, self._seen_so_far, self._size, percentage))
            progressWindow.bar(percentage)
            sys.stdout.flush()


def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def uploadAudioToS3Bucket(fullPath, notebook):
    value.program_status = 'AUDIO_UPLOADING'
    progressWindow.bar(0)
    progressWindow.status_label.config(text="Uploading audio file to transcribe")

    file_name = os.path.split(fullPath)[1]
    bucket = 'research-project-sliit'
    region = 'ap-south-1'
    folder = 'audio/'

    s3 = boto3.client('s3')
    with open(fullPath, "rb") as f:
        s3.upload_file(
            fullPath, bucket, folder + '' + file_name,
            Callback=ProgressPercentage(fullPath)
        )

        url = f"https://{bucket}.s3.{region}.amazonaws.com/{folder}{file_name}"
        utils.constants.uploaded_audio_s3_path = url
        tkinter.messagebox.showinfo(title='Success', message='successfully upload audio to ->' + url)
        getTranscribedJson(notebook)

    return True
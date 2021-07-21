import threading
import time
import tkinter.messagebox

import utils
from utils import value
from utils.aws.uploaders import uploadAudioToS3Bucket
from utils.converters.videoToAudioConverter import videoToAudioConverter


def audioConvertFunc(notebook):
    value.program_status = 'VIDEO_TO_AUDIO_CONVERTING'


    current_time = time.time()
    utils.constants.current_time = str(int(current_time));

    success = False;
    success = videoToAudioConverter(utils.constants.new_video_import_path, current_time)

    if success:
        uploadAudioToS3Bucket(utils.constants.converted_audio_path, notebook)


def transcribeMediator(notebook):
    # extractDataFromResponseJSON("C:\\Users\\User\\Desktop\\newResearch\\2021-064\\tempStorage\\responseJSON\\1625568008.json")
    # Need to uncomment
    if value.program_status == 'VIDEO_FILE_SELECTED':
        threading.Thread(target=audioConvertFunc, args=(notebook,),daemon=True).start()
    else:
        value.program_status = 'ERROR'
        tkinter.messagebox.showinfo(title='Error', message='Please choose a video file first.')
        return

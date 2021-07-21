import os
import tkinter.messagebox

import moviepy.editor as mp

import utils
from utils import CustLog


def videoToAudioConverter(imported_video_path, current_time):

    if imported_video_path:
        my_clip = mp.VideoFileClip(r"" + imported_video_path)

        current_dir = os.path.abspath(os.curdir)

        audio_full_path = current_dir + "/tempStorage\convertedAudio/" + str(int(current_time))+".mp3"
        loger= CustLog.MyBarLogger()
        my_clip.audio.write_audiofile(r"" + audio_full_path,logger = loger)
        utils.constants.converted_audio_path = audio_full_path
        tkinter.messagebox.showinfo(title='Success', message='Video converted to audio successfully')
        my_clip.close()
        return True
    else:
        return False

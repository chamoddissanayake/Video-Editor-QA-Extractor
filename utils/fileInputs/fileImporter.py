import os
import shutil
import tkinter.messagebox
from pathlib import Path
from tkinter import filedialog

import utils
from components.subComponents import Player
from components.subComponents import progressWindow
from utils import value


def file_choose_video(vidImportLbl):
    source = filedialog.askopenfilename(initialdir="/", title="Select Video file",
                                        filetypes=(("Video Files", "*.mp4"),))

    dir_parts = list(os.path.split(source))
    target_dir = dir_parts[0] + '/' + dir_parts[1]
    new_video_import_path = str(Path.cwd()) + "/tempStorage/importVideo/" + dir_parts[1]
    shutil.copy(target_dir, new_video_import_path)
    tkinter.messagebox.showinfo(title='Success', message='Video imported successfully')
    utils.constants.new_video_import_path = new_video_import_path
    value.program_status = "VIDEO_FILE_SELECTED"
    utils.constants.hasVideo = True

    has_chat_path = False if utils.constants.chat_import_path == '' else True

    progressWindow.chatAndVideoSelectStatus(True, has_chat_path)
    Player.play_default_or_selected_video()

    vidImportLbl.set(dir_parts[1])
    return True


def file_choose_chat_export(chatImportLbl):
    source = filedialog.askopenfilename(initialdir="/", title="Select Zoom chat export file",
                                        filetypes=(('text files', 'txt'),))

    dir_parts = list(os.path.split(source))
    target_dir = dir_parts[0] + '/' + dir_parts[1]

    isZoomExport = validateInportChat(target_dir)

    if isZoomExport:
        new_chat_import_path = str(Path.cwd()) + "/tempStorage/importChat"
        shutil.copy(target_dir, new_chat_import_path)

        tkinter.messagebox.showinfo(title='Success', message='Chat export file imported successfully')
        utils.constants.chat_import_path = new_chat_import_path + "/" + dir_parts[1]

        utils.constants.hasChatExport = True

        progressWindow.chatAndVideoSelectStatus(utils.constants.hasVideo, True)
        chatImportLbl.set(dir_parts[1])

    return True


def file_choose_thumbnail(thumbnailImportLbl):
    source = filedialog.askopenfilename(initialdir="/", title="Select file as a Thumbnail",
                                        filetypes=(("Thumbnail Image", "*.jpg"),))

    dir_parts = list(os.path.split(source))
    target_dir = dir_parts[0] + '/' + dir_parts[1]
    thumbnail_path = str(Path.cwd()) + "/tempStorage/thumbnail"
    shutil.copy(target_dir, thumbnail_path)
    tkinter.messagebox.showinfo(title='Success', message='Thumbnail imported successfully')
    utils.constants.thumbnail_path = thumbnail_path + "/" + dir_parts[1]
    thumbnailImportLbl.set(dir_parts[1])

    return True


def validateInportChat(target_dir):
    try:
        with open(target_dir) as f:
            lines = f.readlines()
            for row in lines:
                askedTime = row[:8]
                rest = row[9:].strip()
                msg = rest.split(":")[1].strip()
                mgsTo = rest.split(":")[0].strip().split('to')[1].strip()
                msgFrom = rest.split(":")[0].strip().split('to')[0].strip().replace('From', '').strip()

        return True
    except:
        tkinter.messagebox.showinfo(title='Error', message='Not a valid zoom chat export file.')
        return False

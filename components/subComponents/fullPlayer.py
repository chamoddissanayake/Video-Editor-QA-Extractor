import os
import tkinter as tk
from tkinter import *
from tkinter import font as tkFont

from components.subComponents import Player
from functions.qa import transcribeHandler
from functions.qa.responseJSONHandler import extractDataFromResponseJSON
from utils.fileInputs import fileImporter


def getFullPalyerView(notebook):
    Player.getView(notebook)

    helv10 = tkFont.Font(family='Helvetica', size=10)

    vidImportLbl = StringVar()
    label_vid_choose_state = Label(notebook, textvariable=vidImportLbl, relief=FLAT)
    vidImportLbl.set("")
    label_vid_choose_state.place(x=640, y=65);

    icon_v_file = PhotoImage(file=os.path.abspath(os.curdir) + "/assets/icons/buttons/video-files.png")
    choose_v_file_btn = tk.Button(notebook, image=icon_v_file, text=" Choose Video File...", compound=LEFT, width=175,
                                  height=24, relief=RAISED,
                                  font=helv10, command=lambda: fileImporter.file_choose_video(vidImportLbl));

    choose_v_file_btn.image = icon_v_file
    choose_v_file_btn.place(x=450, y=60)

    chatImportLbl = StringVar()
    label_chat_choose_state = Label(notebook, textvariable=chatImportLbl, relief=FLAT)
    chatImportLbl.set("")
    label_chat_choose_state.place(x=640, y=105);

    icon_c_ex_file = PhotoImage(file=os.path.abspath(os.curdir) + "/assets/icons/buttons/document.png")
    choose_c_ex_file_btn = tk.Button(notebook, image=icon_c_ex_file, text=' Choose Chat Export File...', compound=LEFT,
                                     width=175, height=24, relief=RAISED,
                                     font=helv10, command=lambda: fileImporter.file_choose_chat_export(chatImportLbl))
    choose_c_ex_file_btn.image = icon_c_ex_file
    choose_c_ex_file_btn.place(x=450, y=100)


    icon_transcribe = PhotoImage(file=os.path.abspath(os.curdir) + "/assets/icons/buttons/voice-recognition.png")
    transcribe_btn = tk.Button(notebook, image=icon_transcribe, text=' Transcribe', compound=LEFT, width=175, height=24,
                               relief=RAISED,
                               font=helv10, command=lambda: transcribeHandler.transcribeMediator(notebook))
    transcribe_btn.image = icon_transcribe
    transcribe_btn.place(x=450, y=140)

    # If needed, uncomment
    transcribe_btn = tk.Button(notebook, text='tempTranscribe',
                               command=lambda: extractDataFromResponseJSON(
                                   # "C:/Users/User/Desktop/2021-064\\tempStorage\\responseJSON\\1626449776.json"))
                                   "C:/Users/User/Desktop/newResearch/2021-064\\tempStorage\\responseJSON\\1626449776.json"))
    transcribe_btn.place(x=450, y=180)

    helv11 = tkFont.Font(family='Helvetica', size=13, weight=tkFont.BOLD)

    icon_export = PhotoImage(file=os.path.abspath(os.curdir) + "/assets/icons/buttons/export.png")
    export_btn = tk.Button(notebook, image=icon_export, text='Export >>', compound=TOP, width=100, height=120,
                           relief=RAISED, font=helv11)
    export_btn.image = icon_export
    export_btn.place(x=1350, y=150)

    return notebook

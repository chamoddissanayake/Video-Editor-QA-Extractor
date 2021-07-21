import datetime
import os
import tkinter as tk
from tkinter import *
from tkinter import font as tkFont
from tkinter import ttk

import utils.constants
from components.subComponents import progressWindow, addExtraQuestionsWindow, AdPlayer
from components.subComponents.Player import OnTimeChange
from functions.qa import questionDetectorAndAnswerHandler
from utils import value

selectedItem = 0

listbox = None
transcript_loaded = FALSE
all_sentence_arr = []

speaker_type = ""
sentence_start_time = ""
sentence_end_time = ""
sentence_string = ""


def callback(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)


def getTranscribeWindowView(notebook):
    global listbox
    nb = notebook

    frm1 = ttk.Frame(notebook)

    sby = Scrollbar(notebook)
    label = tk.Label(notebook)

    listbox = tk.Listbox(notebook, yscrollcommand=sby.set, width=70, height=22)
    sbx = Scrollbar(notebook, orient=HORIZONTAL, command=listbox.xview)
    listbox.configure(yscrollcommand=sbx.set)

    listbox.place(x=20, y=10)

    if transcript_loaded:
        for item in all_sentence_arr:
            listbox.insert("end", item.get_sentenceStr())

    listbox.bind("<<ListboxSelect>>", callback)

    extraQCountLbl = StringVar()
    label_extra_q_count = Label(notebook, textvariable=extraQCountLbl, relief=FLAT)
    extraQCountLbl.set("0")
    label_extra_q_count.place(x=660, y=185);

    helv10 = tkFont.Font(family='Helvetica', size=10, weight=tkFont.BOLD)

    extra_q = PhotoImage(file=os.path.abspath(os.curdir) + "/assets/icons/buttons/question.png")
    extract_questions_and_answers_btn = tk.Button(notebook, image=extra_q, text=' Add Extra questions   +',
                                                  compound=LEFT, width=185, height=24, relief=RAISED, font=helv10,
                                                  command=lambda: addExtraQuestionsWindow.addExtraQuestionsPopup(
                                                      extraQCountLbl))
    extract_questions_and_answers_btn.image = extra_q
    extract_questions_and_answers_btn.place(x=460, y=180)

    extract_q = PhotoImage(file=os.path.abspath(os.curdir) + "/assets/icons/buttons/search.png")
    extract_questions_btn = tk.Button(notebook, image=extract_q, text='   Extract Questions', compound=LEFT, width=185,
                                      height=24, relief=RAISED, font=helv10,
                                      command=lambda: questionDetectorAndAnswerHandler.questionDetectorAndAnswerHandlerMediator(
                                          notebook))
    extract_questions_btn.image = extract_q
    extract_questions_btn.place(x=460, y=220)

    extract_q_temp = PhotoImage(file=os.path.abspath(os.curdir) + "/assets/icons/buttons/search.png")
    extract_questions_btn_temp = tk.Button(notebook, image=extract_q_temp, text='   Temp', compound=LEFT, width=185,
                                           height=24, relief=FLAT, font=helv10,
                                           command=lambda: questionDetectorAndAnswerHandler.tempQuestionDetectorAndAnswerHandlerMediator(
                                               notebook))
    extract_questions_btn_temp.image = extract_q_temp
    extract_questions_btn_temp.place(x=460, y=260)

    extract_q_temp = PhotoImage(file=os.path.abspath(os.curdir) + "/assets/icons/buttons/search.png")
    extract_questions_btn_temp = tk.Button(notebook, image=extract_q_temp, text='   Temp Popup', compound=LEFT,
                                           width=185,
                                           height=24, relief=FLAT, font=helv10,
                                           command=lambda: AdPlayer.showAdPopup())
    extract_questions_btn_temp.image = extract_q_temp
    extract_questions_btn_temp.place(x=460, y=300)

    return frm1


def fillTranscriptWindow():
    global all_sentence_arr, listbox, speaker_type, sentence_start_time, sentence_end_time, sentence_string, sentence_start_time_as_num, sentence_end_time_as_num
    all_sentence_arr = utils.constants.all_sentences_obj_arr
    progressWindow.status_label.config(text="Filling transcript window")

    for item in all_sentence_arr:
        speaker_type = item.get_sentenceSpeakerType()
        sentence_start_time = str(datetime.timedelta(seconds=int(item.get_sentenceStartTime())))
        sentence_end_time = str(datetime.timedelta(seconds=int(item.get_sentenceEndTime())))
        sentence_string = item.get_sentenceStr()

        sentence_start_time_as_num = item.get_sentenceStartTime()
        sentence_end_time_as_num = item.get_sentenceEndTime()

        listbox.insert("end",
                       speaker_type + "   " + sentence_start_time + " - " + sentence_end_time + "   " + sentence_string)
    value.program_status = 'TRANSCRIPT_DONE'
    progressWindow.status_label.config(text="Done")


def callback(event):
    global speaker_type, sentence_start_time, sentence_end_time, sentence_string, sentence_start_time_as_num, sentence_end_time_as_num
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        selected_item_obj = utils.constants.all_sentences_obj_arr[index]
        sentence_start_time = selected_item_obj.get_sentenceStartTime()
        OnTimeChange(sentence_start_time)
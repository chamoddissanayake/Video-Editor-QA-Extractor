import os
import tkinter as tk
from tkinter import *
from tkinter import font as tkFont
from tkinter import ttk

from functions.qa import fileGenerateMediator
from utils import constants
from utils.aws import finishedFileUploader
from utils.fileInputs import fileImporter


def getExtractedQuestionsAndAnswersWindow(notebook):
    global qalistbox

    frm1 = ttk.Frame(notebook)

    qalistbox = tk.Listbox(notebook, width=100, height=22)

    qalistbox.place(x=690, y=10)

    helv11 = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD)
    helv13 = tkFont.Font(family='Helvetica', size=13, weight=tkFont.BOLD)

    filesGeneratedLbl = StringVar()
    label_generate_files = Label(notebook, textvariable=filesGeneratedLbl, relief=FLAT)
    filesGeneratedLbl.set("")
    label_generate_files.place(x=1360, y=105);

    icon_generate_file = PhotoImage(file=os.path.abspath(os.curdir) + "/assets/icons/buttons/generate_files.png")
    generateFilesBtn = tk.Button(notebook, image=icon_generate_file, text=' Generate Files', compound=LEFT, width=160,
                                 height=24,
                                 relief=RAISED, font=helv11,
                                 command=lambda: fileGenerateMediator.fileGenerateMediatorFunc(filesGeneratedLbl))
    generateFilesBtn.image = icon_generate_file
    generateFilesBtn.place(x=1320, y=70)

    thumbnailImportLbl = StringVar()
    label_thumbnail_choose_state = Label(notebook, textvariable=thumbnailImportLbl, relief=FLAT)
    thumbnailImportLbl.set("")
    label_thumbnail_choose_state.place(x=1350, y=180);

    icon_thumbnail = PhotoImage(file=os.path.abspath(os.curdir) + "/assets/icons/buttons/thumbnail.png")
    import_thumbnailBtn = tk.Button(notebook, image=icon_thumbnail, text=' Import Thumbnail', compound=LEFT, width=160,
                                    height=24,
                                    relief=RAISED, font=helv11,
                                    command=lambda: fileImporter.file_choose_thumbnail(thumbnailImportLbl))
    import_thumbnailBtn.image = icon_thumbnail
    import_thumbnailBtn.place(x=1320, y=150)

    filesUploadedLbl = StringVar()
    label_Uploaded_files = Label(notebook, textvariable=filesUploadedLbl, relief=FLAT)
    filesUploadedLbl.set("")
    label_Uploaded_files.place(x=1380, y=290);

    icon_upload = PhotoImage(file=os.path.abspath(os.curdir) + "/assets/icons/buttons/upload.png")
    upload_btn = tk.Button(notebook, image=icon_upload, text='Upload', compound=LEFT, width=160, height=64,
                           relief=RAISED, font=helv13,
                           command=lambda: finishedFileUploader.finishedFileUploaderFunc(filesUploadedLbl))
    upload_btn.image = icon_upload
    upload_btn.place(x=1320, y=220)

    return frm1


def lineColorSetter(cl):
    global counter, numberColorArr
    numberColorArr.append({"number": counter, "color": cl})
    counter += 1


def fillColor():
    global qalistbox, counter, numberColorArr
    for i, item in enumerate(numberColorArr):
        qalistbox.itemconfig(i, {'bg': item['color']})


def fillQuestionAnswersWindowFunc():
    global qalistbox, counter, numberColorArr

    counter = 0;
    numberColorArr = []

    if len(constants.video_q_with_a) > 0:
        qalistbox.insert("end",
                         "---------------------------------------- Answers for questions in Video ----------------------------------------")
        lineColorSetter(constants.qa_window_title_color)
        internalCounter1 = 0
        for currentItem in constants.video_q_with_a:
            questionDisplayText = str(currentItem['startTime']) + " " + currentItem[
                'speakerType'].capitalize() + " ->" + currentItem['question']
            qalistbox.insert("end", "Question->" + questionDisplayText)
            lineColorSetter(constants.qa_window_question_color)

            if currentItem['has_lecturer_answer']:
                qalistbox.insert("end", "Lecturer Answer ->" + currentItem['lecturer_answer'])
                lineColorSetter(constants.qa_window_lecturer_answer_color)

            if currentItem['checked']:
                for ans in currentItem['google_answer']:
                    qalistbox.insert("end", "Answer ->" + ans['a'])
                    lineColorSetter(constants.qa_window_google_answer_color)
                    qalistbox.insert("end", "Site ->" + ans['cited'])
                    lineColorSetter(constants.qa_window_google_answer_color)
            internalCounter1 += 1
            if internalCounter1 != len(constants.video_q_with_a):
                qalistbox.insert("end",
                                 "----------------------------------------------------------------------------------------------------------------------")
                lineColorSetter(constants.qa_window_empty_line_color)
        qalistbox.insert("end",
                         "============================================================================================================")
        lineColorSetter(constants.qa_window_empty_line_color)

    if len(constants.chat_q_with_a) > 0:
        qalistbox.insert("end",
                         "------------------------------------------- Answers for questions in Chat -------------------------------------------")
        internalCounter2 = 0
        lineColorSetter(constants.qa_window_title_color)
        qalistbox.insert("end", "Question ->" + currentItem['question'])
        lineColorSetter(constants.qa_window_question_color)

        if currentItem['has_lecturer_answer']:
            qalistbox.insert("end", "Lecturer Answer ->" + currentItem['lecturer_answer'])
            lineColorSetter(constants.qa_window_lecturer_answer_color)

        if currentItem['checked']:
            for currentItem in constants.chat_q_with_a:
                for ans in currentItem['google_answer']:
                    qalistbox.insert("end", "Answer ->" + ans['a'])
                    lineColorSetter(constants.qa_window_google_answer_color)
                    qalistbox.insert("end", "Site ->" + ans['cited'])
                    lineColorSetter(constants.qa_window_google_answer_color)
                internalCounter2 += 1
                if internalCounter2 != len(constants.chat_q_with_a):
                    qalistbox.insert("end",
                                     "----------------------------------------------------------------------------------------------------------------------")
                    lineColorSetter(constants.qa_window_empty_line_color)
        qalistbox.insert("end",
                         "===============================================================================================")
        lineColorSetter(constants.qa_window_empty_line_color)

    if len(constants.manual_q_with_a) > 0:
        qalistbox.insert("end",
                         "------------------------------------------- Answers for Manually Added questions -------------------------------------------")
        lineColorSetter(constants.qa_window_title_color)
        internalCounter3 = 0
        for currentItem in constants.manual_q_with_a:

            qalistbox.insert("end", "Question ->" + currentItem['question'])
            lineColorSetter(constants.qa_window_question_color)

            if currentItem['lecturer_answer'] != "":
                qalistbox.insert("end", "Lecturer Answer ->" + currentItem['lecturer_answer'])
                lineColorSetter(constants.qa_window_lecturer_answer_color)

            if len(currentItem['google_answer']):
                for ans in currentItem['google_answer']:
                    qalistbox.insert("end", "Answer ->" + ans['a'])
                    lineColorSetter(constants.qa_window_google_answer_color)
                    qalistbox.insert("end", "Site ->" + ans['cited'])
                    lineColorSetter(constants.qa_window_google_answer_color)
            internalCounter3 += 1
            if internalCounter3 != len(constants.manual_q_with_a):
                qalistbox.insert("end",
                                 "--------------------------------------------------------------------------------------------------")
                lineColorSetter(constants.qa_window_empty_line_color)
        qalistbox.insert("end",
                         "============================================================================================================")
        lineColorSetter(constants.qa_window_empty_line_color)
    fillColor()

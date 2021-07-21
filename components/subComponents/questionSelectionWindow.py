import os
import threading
import time
import tkinter as tk
from tkinter import *
from tkinter import font as tkFont

from components.subComponents import progressWindow
from components.subComponents.temp import ScrollableFrame
from utils import constants, general
from utils import value
from utils.ToolTip import CreateToolTip
from utils.general import getSplittedSentece, getCheckedInBool
from utils.google import answerExtractor


def questionSelectorWindowFuc(notebook):
    w = popupWindow(notebook)
    notebook.wait_window(w.top)


class popupWindow(object):
    def __init__(self, master):
        self.top = top = Toplevel(master)

        for i in range(50):
            cb = Checkbutton(top, text="checkbutton %s" % i, padx=0, pady=0, bd=0)
            cb.pack()
        self.b = Button(top, text='Ok')
        self.b.pack()


def extractedQuestionsSelectionPopup():
    global enable_vid, enable_chat, enable_manual, selectedAllVarCB, selectedAllVidVarCB, selectedAllChatVarCB, selectedAllManualVarCB, \
        selectedAllVar, selectedAllVidVar, selectedAllChatVar, selectedAllManualVar, win

    win = tk.Toplevel()

    windowWidth = win.winfo_reqwidth()
    windowHeight = win.winfo_reqheight()

    positionRight = int(win.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(win.winfo_screenheight() / 4 - windowHeight / 2)

    win.geometry("+{}+{}".format(positionRight, positionDown))
    win.geometry("300x650+{}+{}".format(positionRight, positionDown))

    win.wm_title("Found Questions")

    selectedAllVar = Variable();
    selectedAllVar.set(1)
    selectedAllVarCB = Checkbutton(win, text="Select All / None", command=pressedSelectAll)
    selectedAllVarCB.pack()
    selectedAllVarCB.select()

    tk.Label(win, text="------------Extracted Questions in video------------").pack()

    selectedAllVidVar = Variable()
    selectedAllVidVar.set(1)
    selectedAllVidVarCB = Checkbutton(win, text="Select All / None", command=pressedSelectAllInVideoQuestions)
    selectedAllVidVarCB.pack()
    selectedAllVidVarCB.select()

    checkbox_pane_vid = ScrollableFrame(win)
    checkbox_pane_vid.pack(expand="true", fill="both")

    enable_vid = []

    for videoQuestionItem in constants.video_file_question_arr:
        enable_vid.append({
            "question": videoQuestionItem.question,
            "checked": True,
            "endTime": videoQuestionItem.endTime,
            "google_answer": videoQuestionItem.google_answer,
            "has_lecturer_answer": videoQuestionItem.has_lecturer_answer,
            "question": videoQuestionItem.question,
            "sentence_type": videoQuestionItem.sentence_type,
            "speakerType": videoQuestionItem.speakerType,
            "startTime": videoQuestionItem.startTime,
            "lecturer_answer": videoQuestionItem.lecturer_answer,
            "is_saying_chat_q": videoQuestionItem.is_saying_chat_q,
            "is_saying_chat_str": videoQuestionItem.is_saying_chat_str
        })

    for item_vid in enable_vid:
        if item_vid['has_lecturer_answer'] == True and item_vid['is_saying_chat_q'] == False:
            item_vid["checked"] = Variable()
            item_vid["checked"].set(1)
            l_vid = Checkbutton(checkbox_pane_vid.interior, text="👨 ✔️" + item_vid["question"],
                                variable=item_vid["checked"], bg="#ffffff", command=singleItemPressed)
            l_vid.pack(anchor=W)
            CreateToolTip(l_vid, text=getSplittedSentece(item_vid['lecturer_answer']))

    for item_vid in enable_vid:
        if item_vid['has_lecturer_answer'] == False and item_vid['is_saying_chat_q'] == False:
            item_vid["checked"] = Variable()
            item_vid["checked"].set(1)
            l_vid = Checkbutton(checkbox_pane_vid.interior, text=item_vid["question"], variable=item_vid["checked"],
                                bg="#ffffff", command=singleItemPressed)
            l_vid.pack(anchor=W)

    tk.Label(win, text="------------Extracted Questions in Chat File------------").pack()

    selectedAllChatVar = Variable()
    selectedAllChatVar.set(1)

    selectedAllChatVarCB = Checkbutton(win, text="Select All / None", command=pressedSelectAllInChatQuestions)
    selectedAllChatVarCB.pack()
    selectedAllChatVarCB.select()

    checkbox_pane_chat = ScrollableFrame(win)
    checkbox_pane_chat.pack(expand="true", fill="both")

    enable_chat = []

    for chatQuestionItem in constants.chat_file_question_arr:
        enable_chat.append({
            "question": chatQuestionItem.question,
            "has_lecturer_answer": chatQuestionItem.has_lecturer_answer,
            "question_type": chatQuestionItem.question_type,
            "receiver": chatQuestionItem.receiver,
            "sender": chatQuestionItem.sender,
            "lecturer_answer": chatQuestionItem.lecturer_answer,
            "timestamp": chatQuestionItem.timestamp,
            "checked": True
        })


    for item_chat in enable_chat:
        if item_chat['has_lecturer_answer']:
            item_chat["checked"] = Variable()
            item_chat["checked"].set(1)
            l_chat = Checkbutton(checkbox_pane_chat.interior, text="👨 ✔️" + item_chat["question"],
                                 variable=item_chat["checked"],
                                 bg="#ffffff", command=singleItemPressed)
            l_chat.pack(anchor=W)

            CreateToolTip(l_chat, text=getSplittedSentece(item_chat['lecturer_answer']))

    for item_chat in enable_chat:
        if item_chat['has_lecturer_answer'] == False:
            item_chat["checked"] = Variable()
            item_chat["checked"].set(1)
            l_chat = Checkbutton(checkbox_pane_chat.interior, text=item_chat["question"], variable=item_chat["checked"],
                                 bg="#ffffff", command=singleItemPressed)
            l_chat.pack(anchor=W)

    tk.Label(win, text="------------Manually added Questions------------").pack()

    selectedAllManualVar = Variable()
    selectedAllManualVar.set(1)

    selectedAllManualVarCB = Checkbutton(win, text="Select All / None", command=pressedSelectAllInManualQuestions)
    selectedAllManualVarCB.pack()
    selectedAllManualVarCB.select()

    checkbox_pane_manual = ScrollableFrame(win)
    checkbox_pane_manual.pack(expand="true", fill="both")

    enable_manual = []

    for manualQuestionItem in constants.manually_added_question_arr:
        enable_manual.append({
            "question": manualQuestionItem['question'],
            "lecturer_answer": manualQuestionItem['lecturer_answer'],
            "checked": True
        })


    for item_manual in enable_manual:
        if item_manual['lecturer_answer'] != "":
            item_manual["checked"] = Variable()
            item_manual["checked"].set(1)
            l_manual = Checkbutton(checkbox_pane_manual.interior, text="👨 ✔️" + item_manual["question"],
                                   variable=item_manual["checked"],
                                   bg="#ffffff", command=singleItemPressed)
            l_manual.pack(anchor=W)

            CreateToolTip(l_manual, text=getSplittedSentece(item_manual['lecturer_answer']))

    for item_manual in enable_manual:
        if item_manual['lecturer_answer'] == "":
            item_manual["checked"] = Variable()
            item_manual["checked"].set(1)
            l_manual = Checkbutton(checkbox_pane_manual.interior, text=item_manual["question"],
                                   variable=item_manual["checked"], bg="#ffffff", command=singleItemPressed)
            l_manual.pack(anchor=W)

    helv13 = tkFont.Font(family='Helvetica', size=13, weight=tkFont.BOLD)

    icon_search_google = PhotoImage(file=os.path.abspath(os.curdir) + "/assets/icons/buttons/google.png")
    submit_button = tk.Button(win, image=icon_search_google, text=' Find Answers', compound=LEFT, width=140, height=30,
                              relief=FLAT, font=helv13, command=submitPressed)
    submit_button.image = icon_search_google
    submit_button.pack()


def submitPressed():
    global enable_vid, enable_chat, enable_manual, win
    value.program_status = "PREPARING_FOR_FINDING_ANSWERS"
    progressWindow.status_label.config(text="Preparing for finding answers")
    progressWindow.hide_determinate()
    progressWindow.show_indeterminate()

    threading.Thread(target=progressTimerFunc, daemon=True).start()
    enable_vid = general.sort_enable_vid_first_q_with_a_and_then_q_without_a(enable_vid);

    tempArrEnableVid = []
    for enable_vid_index in enable_vid:
        if not isinstance(enable_vid_index['checked'], bool):

            boolStatus = getCheckedInBool(enable_vid_index['checked'].get())

            tempVideoQAObj = {
                'checked': boolStatus,
                'startTime': enable_vid_index['startTime'],
                'endTime': enable_vid_index['endTime'],
                'speakerType': enable_vid_index['speakerType'],
                'question': enable_vid_index['question'],
                'sentence_type': enable_vid_index['sentence_type'],
                'has_lecturer_answer': enable_vid_index['has_lecturer_answer'],
                'lecturer_answer': enable_vid_index['lecturer_answer'],
                'google_answer': enable_vid_index['google_answer'],
                'is_saying_chat_q': enable_vid_index['is_saying_chat_q'],
                'is_saying_chat_str': enable_vid_index['is_saying_chat_str']
            }

            tempArrEnableVid.append(tempVideoQAObj)
        else:
            tempArrEnableVid.append(enable_vid_index)

    enable_vid = tempArrEnableVid

    q_list_vid = []
    for index in range(len(enable_vid)):
        if enable_vid[index]['checked'] == True or enable_vid[index]['has_lecturer_answer'] == True:
            temp_vid = {
                "question": enable_vid[index]['question'],
                "checked": enable_vid[index]['checked'],
                "endTime": enable_vid[index]['endTime'],
                "google_answer": enable_vid[index]['google_answer'],
                "has_lecturer_answer": enable_vid[index]['has_lecturer_answer'],
                "sentence_type": enable_vid[index]['sentence_type'],
                "speakerType": enable_vid[index]['speakerType'],
                "startTime": enable_vid[index]['startTime'],
                "lecturer_answer": enable_vid[index]['lecturer_answer'],
                "is_saying_chat_q": enable_vid[index]['is_saying_chat_q'],
                "is_saying_chat_str": enable_vid[index]['is_saying_chat_str']
            }
            q_list_vid.append(temp_vid)


    enable_chat = general.sort_enable_chat_first_q_with_a_and_then_q_without_a(enable_chat);

    tempArrEnableChat = []
    for enable_chat_index in enable_chat:

        if isinstance(enable_chat_index['checked'], bool):
            tempArrEnableChat.append(enable_chat_index)

        else:
            boolStatus = getCheckedInBool(enable_chat_index['checked'].get())

            tempChatQAObj = {
                "question": enable_chat_index['question'],
                "has_lecturer_answer": enable_chat_index['has_lecturer_answer'],
                "question_type": enable_chat_index['question_type'],
                "receiver": enable_chat_index['receiver'],
                "sender": enable_chat_index['sender'],
                "lecturer_answer": enable_chat_index['lecturer_answer'],
                "timestamp": enable_chat_index['timestamp'],
                "checked": boolStatus
            }

            tempArrEnableChat.append(tempChatQAObj)

    enable_chat = tempArrEnableChat

    q_list_chat = []
    for i, q_chat in enumerate(enable_chat):
        if q_chat["checked"] == 1 or enable_chat[i]['has_lecturer_answer'] == True:
            q_temp_chat = {
                "question": q_chat.get('question'),
                "has_lecturer_answer": q_chat.get('has_lecturer_answer'),
                "question_type": q_chat.get('question_type'),
                "receiver": q_chat.get('receiver'),
                "sender": q_chat.get('sender'),
                "lecturer_answer": q_chat.get('lecturer_answer'),
                "timestamp": q_chat.get('timestamp'),
                "checked": getCheckedInBool(q_chat.get('checked'))
            }
            q_list_chat.append(q_temp_chat)



    tempArrEnableManual = []
    for enable_manual_index in enable_manual:

        if isinstance(enable_manual_index['checked'], bool):
            tempArrEnableManual.append(enable_manual_index)

        else:
            boolStatus = getCheckedInBool(enable_manual_index['checked'].get())

            tempManualQAObj = {
                "question": enable_manual_index['question'],
                "lecturer_answer": enable_manual_index['lecturer_answer'],
                "checked": boolStatus
            }

            tempArrEnableManual.append(tempManualQAObj)

    enable_manual = tempArrEnableManual

    q_list_manual = []
    for q_manual in enable_manual:
        q_temp_manual = {
            "question": q_manual['question'],
            "lecturer_answer": q_manual['lecturer_answer'],
            "google_answer": [],
            "checked": q_manual['checked']
        }
        q_list_manual.append(q_temp_manual)


    constants.ready_to_find_answers_video_questions = q_list_vid
    constants.ready_to_find_answers_chat_questions = q_list_chat
    constants.ready_to_find_answers_manual_questions = q_list_manual

    progressWindow.hide_indeterminate()
    progressWindow.show_determinate()

    answerExtractor.findAnswersFromGoogleMediator()
    win.destroy()


def pressedSelectAll():
    global enable_vid, enable_chat, enable_manual, \
        selectedAllVarCB, selectedAllVidVarCB, selectedAllChatVarCB, selectedAllManualVarCB, \
        selectedAllVar, selectedAllVidVar, selectedAllChatVar, selectedAllManualVar

    if selectedAllVar == True:
        selectedAllVarCB.deselect();
        selectedAllVidVarCB.deselect();
        selectedAllChatVarCB.deselect();
        selectedAllManualVarCB.deselect();

        selectedAllVar.set(0)
        selectedAllVidVar.set(0)
        selectedAllChatVar.set(0)
        selectedAllManualVar.set(0)
        for vidItem in enable_vid:
            vidItem["checked"].set(0)
        for chatItem in enable_chat:
            chatItem["checked"].set(0)
        for manualItem in enable_manual:
            manualItem["checked"].set(0)
    else:
        selectedAllVarCB.select();
        selectedAllVidVarCB.select();
        selectedAllChatVarCB.select();
        selectedAllManualVarCB.select();
        selectedAllVar.set(1)
        selectedAllVidVar.set(1)
        selectedAllChatVar.set(1)
        selectedAllManualVar.set(1)
        for vidItem in enable_vid:
            vidItem["checked"].set(1)
        for chatItem in enable_chat:
            chatItem["checked"].set(1)
        for manualItem in enable_manual:
            manualItem["checked"].set(1)


def pressedSelectAllInVideoQuestions():
    global enable_vid, enable_chat, enable_manual, selectedAllVidVar
    if selectedAllVidVar == True:
        selectedAllVidVar.set(0)
        for vidItem in enable_vid:
            vidItem["checked"].set(0)
    else:
        selectedAllVidVar.set(1)
        for vidItem in enable_vid:
            vidItem["checked"].set(1)


def pressedSelectAllInChatQuestions():
    global enable_vid, enable_chat, enable_manual, selectedAllChatVar

    if selectedAllChatVar == True:
        selectedAllChatVar.set(0)
        for chatItem in enable_chat:
            chatItem["checked"].set(0)
    else:
        selectedAllChatVar.set(1)
        for chatItem in enable_chat:
            chatItem["checked"].set(1)


def pressedSelectAllInManualQuestions():
    global enable_vid, enable_chat, enable_manual, selectedAllManualVar

    if selectedAllManualVar == True:
        selectedAllManualVar.set(0)
        for manualItem in enable_manual:
            manualItem["checked"].set(0)
    else:
        selectedAllManualVar.set(1)
        for manualItem in enable_manual:
            manualItem["checked"].set(1)


def progressTimerFunc():
    progressWindow.barIndeterminate()
    time.sleep(0.5)
    progressWindow.barIndeterminate()
    time.sleep(0.5)
    progressWindow.barIndeterminate()


def singleItemPressed():
    global selectedAllVidVarCB, selectedAllManualVarCB

    enable_vid,

    vidUntickCount = 0
    chatUntickCount = 0
    manualUntickCount = 0
    mainUntickCount = 0

    for v in enable_vid:
        if int(v["checked"]) == False:
            vidUntickCount += 1
            mainUntickCount += 1

    for v in enable_chat:
        if int(v["checked"]) == False:
            chatUntickCount += 1
            mainUntickCount += 1

    for v in enable_manual:
        if int(v["checked"]) == False:
            manualUntickCount += 1
            mainUntickCount += 1

    if mainUntickCount == 0:
        selectedAllVar.set(1)
        selectedAllVarCB.select()
    else:
        selectedAllVar.set(0)
        selectedAllVarCB.deselect()

    if vidUntickCount == 0:
        selectedAllVidVar.set(1)
    else:
        selectedAllVidVar.set(0)

    if chatUntickCount == 0:
        selectedAllChatVar.set(1)
    else:
        selectedAllChatVar.set(0)

    if manualUntickCount == 0:
        selectedAllManualVar.set(1)
        selectedAllManualVarCB.select()
    else:
        selectedAllManualVar.set(0)
        selectedAllManualVarCB.deselect()

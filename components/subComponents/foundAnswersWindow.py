import tkinter as tk
from tkinter import *

from components.subComponents import extractedQuestionsAnswersWindow, progressWindow
from components.subComponents.temp import ScrollableFrame
from utils import constants
from utils.ToolTip import CreateToolTip
from utils.general import getSplittedSentece


def showFoundAnswersWindow():
    global win, vidTxtBoxArr1,vidTxtBoxArr2, chatTxtBoxArr1, chatTxtBoxArr2, manualTxtBoxArr1, manualTxtBoxArr2

    progressWindow.status_label.config(text="Done")
    win = tk.Toplevel()

    windowWidth = win.winfo_reqwidth()
    windowHeight = win.winfo_reqheight()

    positionRight = int(win.winfo_screenwidth() / 3 - windowWidth / 2)
    positionDown = int(win.winfo_screenheight() / 4 - windowHeight / 2)

    win.geometry("+{}+{}".format(positionRight, positionDown))
    win.geometry("660x650+{}+{}".format(positionRight, positionDown))

    win.wm_title("Found Answers")

    tk.Label(win,font='Helvetica 11 bold', text="------------------------------------------ Answers for Video Questions ---------------------------------------------").pack()

    pane_vid = ScrollableFrame(win, bg='#f7f7f7')
    pane_vid.pack(expand="true", fill="both")

    vidTxtBoxArr1 = []
    vidTxtBoxArr2 = []

    for i, item_vid in enumerate(constants.video_q_with_a):
        if item_vid['is_saying_chat_q'] == False:

            Label(pane_vid.interior, text=item_vid['question']).pack()

            if item_vid['has_lecturer_answer']:
                if len(item_vid['lecturer_answer']) > 160:
                    txtHeight = 4
                else:
                    txtHeight = 2

                inputtxt1 = Text(pane_vid.interior, height=txtHeight, bg="#F0E68C")
                inputtxt1.insert(tk.END, item_vid['lecturer_answer'])
                inputtxt1.pack()
                CreateToolTip(inputtxt1, text=getSplittedSentece("This answer was given by the lecturer"))
                vidTxtBoxArr1.append({"i": i,
                                      "lecturer_answer": inputtxt1,
                                      "question" :item_vid['question']
                                      })

            if item_vid['checked']:
                for loopCount, answer in enumerate(item_vid['google_answer']):
                    if len(answer) > 160:
                        txtHeight = 4
                    else:
                        txtHeight = 2

                    inputtxt2 = Text(pane_vid.interior, height=txtHeight,bg="#ffffff")
                    inputtxt2.insert(tk.END, answer['a'] + answer['cited'])
                    inputtxt2.pack()
                    vidTxtBoxArr2.append({"i":i,
                                          "question" :item_vid['question'],
                                          "google_answer": inputtxt2,
                                          "c":item_vid['google_answer'][loopCount]['cited']})



    tk.Label(win,font='Helvetica 11 bold', text="------------------------------------------- Answers for chat questions ----------------------------------------------").pack()

    pane_chat = ScrollableFrame(win, bg='#f7f7f7')
    pane_chat.pack(expand="true", fill="both")

    chatTxtBoxArr1 = []
    chatTxtBoxArr2 = []
    for j, item_chat in enumerate(constants.chat_q_with_a):
        Label(pane_chat.interior, text=item_chat['question']).pack()
        if item_chat['has_lecturer_answer']:
            if len(item_chat['lecturer_answer']) > 160:
                txtHeight = 4
            else:
                txtHeight = 2

            inputtxt1 = Text(pane_chat.interior, height=txtHeight, bg="#F0E68C")
            inputtxt1.insert(tk.END, item_chat['lecturer_answer'])
            inputtxt1.pack()
            CreateToolTip(inputtxt1, text=getSplittedSentece("This answer was given by the lecturer"))
            chatTxtBoxArr1.append({"i": i,
                                  "lecturer_answer": inputtxt1,
                                  "question" :item_chat['question']
                                  })

        if item_chat['checked']:
            for loopCount, answer in enumerate(item_chat['google_answer']):
                if len(answer) > 160:
                    txtHeight = 4
                else:
                    txtHeight = 2

                inputtxt2 = Text(pane_chat.interior, height=txtHeight,bg="#ffffff")
                inputtxt2.insert(tk.END, answer['a'] + answer['cited'])
                inputtxt2.pack()
                chatTxtBoxArr2.append({"i":i,
                                      "question" :item_chat['question'],
                                      "google_answer": inputtxt2,
                                      "c":item_chat['google_answer'][loopCount]['cited']})



    tk.Label(win,font='Helvetica 11 bold', text="------------------------------------------- Answers for Manually added questions ----------------------------------------------").pack()

    pane_manual = ScrollableFrame(win, bg='#f7f7f7')
    pane_manual.pack(expand="true", fill="both")

    manualTxtBoxArr1 = []
    manualTxtBoxArr2 = []
    for k, item_manual in enumerate(constants.manual_q_with_a):
        Label(pane_manual.interior, text=item_manual['question']).pack()

        if item_manual['lecturer_answer']!= "":
            if len(item_manual['lecturer_answer']) > 160:
                txtHeight = 4
            else:
                txtHeight = 2

            txtbxManual1 = Text(pane_manual.interior, height=txtHeight, bg="#F0E68C")
            txtbxManual1.insert(tk.END, item_manual['lecturer_answer'])
            txtbxManual1.pack()
            CreateToolTip(txtbxManual1, text=getSplittedSentece("This answer was given by the lecturer"))
            manualTxtBoxArr1.append({"i": i,
                                  "lecturer_answer": txtbxManual1,
                                  "question" :item_manual['question']
                                  })

        if item_manual['checked']:
            if len(item_manual['google_answer']) > 0:
                for loopCount, answer in enumerate(item_manual['google_answer']):
                    if len(answer['a']) > 160:
                        txtHeight = 4
                    else:
                        txtHeight = 2
                    txtbxManual2 = Text(pane_manual.interior, height = txtHeight,  bg="#FFFFFF")
                    txtbxManual2.pack()
                    txtbxManual2.insert(tk.END, answer['a'] +" - "+ answer['cited'])
                    manualTxtBoxArr2.append({"i":i,
                                          "question" :item_manual['question'],
                                          "google_answer": txtbxManual2,
                                          "c":item_manual['google_answer'][loopCount]['cited']})


    tk.Button(win, text="Done", font=30, command=donePressed).pack()



def donePressed():
    global win, vidTxtBoxArr1,vidTxtBoxArr2, chatTxtBoxArr1, chatTxtBoxArr2, manualTxtBoxArr1, manualTxtBoxArr2

    temp1Vid=[]
    for tempItem1 in vidTxtBoxArr1:
        lecturer_answer = tempItem1['lecturer_answer'].get("1.0", "end-1c")
        question = tempItem1['question']
        temp1Vid.append({"question":question, "updated_lecturer_answer":lecturer_answer})

    vidTxtBoxArr1 = temp1Vid

    temp2Vid=[]
    for tempItem2 in vidTxtBoxArr2:
        updated_google_answer = tempItem2['google_answer'].get("1.0", "end-1c")
        question = tempItem2['question']
        cited = tempItem2['c']
        temp2Vid.append({"question":question, "updated_google_answer":updated_google_answer,"cited":cited})

    vidTxtBoxArr2 = temp2Vid

    temp1Chat=[]
    for tempItem1 in chatTxtBoxArr1:
        lecturer_answer = tempItem1['lecturer_answer'].get("1.0", "end-1c")
        question = tempItem1['question']
        temp1Chat.append({"question":question, "updated_lecturer_answer":lecturer_answer})

    chatTxtBoxArr1 = temp1Chat

    temp2Chat=[]
    for tempItem2 in chatTxtBoxArr2:
        updated_google_answer = tempItem2['google_answer'].get("1.0", "end-1c")
        question = tempItem2['question']
        cited = tempItem2['c']
        temp2Chat.append({"question":question, "updated_google_answer":updated_google_answer,"cited":cited})

    chatTxtBoxArr2 = temp2Chat

    # manual

    temp1Manual=[]
    for tempItem1 in manualTxtBoxArr1:
        lecturer_answer = tempItem1['lecturer_answer'].get("1.0", "end-1c")
        question = tempItem1['question']
        temp1Manual.append({"question":question, "updated_lecturer_answer":lecturer_answer})
    #
    manualTxtBoxArr1 = temp1Manual

    temp2Manual=[]
    for tempItem2 in manualTxtBoxArr2:
        updated_google_answer = tempItem2['google_answer'].get("1.0", "end-1c")
        question = tempItem2['question']
        cited = tempItem2['c']
        temp2Manual.append({"question":question, "updated_google_answer":updated_google_answer,"cited":cited})

    manualTxtBoxArr2 = temp2Manual

    finalVideoArr = []
    for constants_video_q_with_a_item in constants.video_q_with_a:
        updatedAns = ""
        for vidTxtBoxArr1Item in vidTxtBoxArr1:
            if vidTxtBoxArr1Item['question']==constants_video_q_with_a_item['question']:
                if constants_video_q_with_a_item['has_lecturer_answer']:
                    updatedAns = vidTxtBoxArr1Item['updated_lecturer_answer']

        newVidTxtBoxArr2=[]
        for vidTxtBoxArr2Item in vidTxtBoxArr2:
            if constants_video_q_with_a_item['question'] == vidTxtBoxArr2Item['question']:
                tempObj = {
                    "a":vidTxtBoxArr2Item['updated_google_answer'],
                    "cited":vidTxtBoxArr2Item['cited']
                }
                newVidTxtBoxArr2.append(tempObj)

        fullUpdatedObj={
            'question':constants_video_q_with_a_item['question'],
            'checked' :constants_video_q_with_a_item['checked'],
            'endTime' :constants_video_q_with_a_item['endTime'],
            'google_answer' :newVidTxtBoxArr2,
            'has_lecturer_answer':constants_video_q_with_a_item['has_lecturer_answer'],
            'sentence_type' :constants_video_q_with_a_item['sentence_type'],
            'speakerType' :constants_video_q_with_a_item['speakerType'],
            'startTime':constants_video_q_with_a_item['startTime'],
            'lecturer_answer':updatedAns
        }
        finalVideoArr.append(fullUpdatedObj)





    # chat

    finalChatArr = []
    for constants_chat_q_with_a_item in constants.chat_q_with_a:

        updatedAns = ""
        for chatTxtBoxArr1Item in chatTxtBoxArr1:
            if chatTxtBoxArr1Item['question']==constants_chat_q_with_a_item['question']:
                if constants_chat_q_with_a_item['has_lecturer_answer']:
                    updatedAns = chatTxtBoxArr1Item['updated_lecturer_answer']

        newChatTxtBoxArr2=[]
        for chatTxtBoxArr2Item  in chatTxtBoxArr2:
            if constants_chat_q_with_a_item['question'] == chatTxtBoxArr2Item['question']:
                tempObj = {
                    "a":chatTxtBoxArr2Item['updated_google_answer'],
                    "cited":chatTxtBoxArr2Item['cited']
                }
                newChatTxtBoxArr2.append(tempObj)


        fullUpdatedObj={
            'question' :constants_chat_q_with_a_item['question'],
            'has_lecturer_answer': constants_chat_q_with_a_item['has_lecturer_answer'],
            'question_type' :constants_chat_q_with_a_item['question_type'],
            'receiver' :constants_chat_q_with_a_item['receiver'],
            'sender' :constants_chat_q_with_a_item['sender'],
            'lecturer_answer':updatedAns,
            'timestamp' :constants_chat_q_with_a_item['lecturer_answer'],
            'checked':constants_chat_q_with_a_item['checked'],
            'google_answer': newChatTxtBoxArr2,

        }
        finalChatArr.append(fullUpdatedObj)



    # manual

    finalManualArr = []
    for constants_manual_q_with_a_item in constants.manual_q_with_a:

        updatedAns = ""
        for manualTxtBoxArr1Item in manualTxtBoxArr1:
            if manualTxtBoxArr1Item['question']==constants_manual_q_with_a_item['question']:
                if constants_manual_q_with_a_item['lecturer_answer']!="":
                    updatedAns = manualTxtBoxArr1Item['updated_lecturer_answer']

        newManualTxtBoxArr2=[]
        for manualTxtBoxArr2Item in manualTxtBoxArr2:
            if constants_manual_q_with_a_item['question'] == manualTxtBoxArr2Item['question']:
                tempObj = {
                    "a":manualTxtBoxArr2Item['updated_google_answer'],
                    "cited":manualTxtBoxArr2Item['cited']
                }
                newManualTxtBoxArr2.append(tempObj)

        fullUpdatedObj={
            'question' :constants_manual_q_with_a_item['question'],
            'lecturer_answer':updatedAns,
            'google_answer': newManualTxtBoxArr2,
            'checked':constants_manual_q_with_a_item['checked']
        }
        finalManualArr.append(fullUpdatedObj)

    constants.video_q_with_a = finalVideoArr
    constants.manual_q_with_a = finalManualArr
    constants.chat_q_with_a = finalChatArr


    win.destroy()
    win.update()

    extractedQuestionsAnswersWindow.fillQuestionAnswersWindowFunc()




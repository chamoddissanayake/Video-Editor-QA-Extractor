import os
import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter import font as tkFont

from utils import constants


def close(win):
    win.destroy()


def addExtraQuestionsPopup(extraQCountLbl):
    global inputtxt_q
    win = tk.Toplevel()

    windowWidth = win.winfo_reqwidth()
    windowHeight = win.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(win.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(win.winfo_screenheight() / 2 - windowHeight / 2)

    # Positions the window in the center of the page.
    win.geometry("+{}+{}".format(positionRight, positionDown))
    win.geometry("300x400+{}+{}".format(positionRight, positionDown))

    win.wm_title("Add more questions")

    def Take_input(extraQCountLbl):

        inputText_q = inputtxt_q.get("1.0", "end-1c")
        inputText_a = inputtxt_a.get("1.0", "end-1c")
        if inputText_q == '':
            tkinter.messagebox.showinfo(title='Error', message='Please enter a question.')
            addExtraQuestionsPopup(len(constants.manually_added_question_arr))
        else:
            constants.manually_added_question_arr.append({
                "question": inputText_q,
                "lecturer_answer": inputText_a
            })

            for question_item in constants.manually_added_question_arr:
                if question_item['lecturer_answer'] == "":
                    lbl_q_without_a = "  Q:  " + question_item['question']
                    listbox.insert(END, lbl_q_without_a)
                else:
                    lbl_q_with_a = "  Q:  " + question_item['question'] + "  |  A:  " + question_item['lecturer_answer']
                    listbox.insert(END, lbl_q_with_a)

            win.destroy()
            extraQCountLbl.set(str(len(constants.manually_added_question_arr)))
            addExtraQuestionsPopup(extraQCountLbl)

    lbl_q = Label(win, text="Question: ")
    inputtxt_q = Text(win, height=2, width=25, bg="white")
    inputtxt_q.bind("<Tab>", focus_next_widget)
    inputtxt_q.bind("<Return>", focus_next_widget)
    lbl_a = Label(win, text="Answer: ")
    inputtxt_a = Text(win, height=2, width=28, bg="white")

    inputtxt_a.bind("<Return>", lambda event, a=extraQCountLbl:
    Take_input(a))

    helv10 = tkFont.Font(family='Helvetica', size=10, weight=tkFont.BOLD)
    add_q = PhotoImage(file=os.path.abspath(os.curdir) + "/assets/icons/buttons/add.png")
    Display = tk.Button(win, image=add_q, text='   Add Question', compound=LEFT, width=185, height=24, relief=RAISED,
                        font=helv10, command=lambda: Take_input(extraQCountLbl))
    Display.image = add_q

    lbl_q.pack()
    inputtxt_q.pack()
    inputtxt_q.focus()
    lbl_a.pack()
    inputtxt_a.pack()
    Display.pack()

    listbox = Listbox(win, width=47)
    listbox.pack(side=LEFT, fill=BOTH)

    if len(constants.manually_added_question_arr) > 0:
        for question in constants.manually_added_question_arr:
            if question['lecturer_answer'] == "":
                lbl_q_without_a = "  Q:  " + question['question']
                listbox.insert(END, lbl_q_without_a)
            else:
                lbl_q_with_a = "  Q:  " + question['question'] + "  |  A:  " + question['lecturer_answer']
                listbox.insert(END, lbl_q_with_a)

    scrollbar = Scrollbar(win)
    scrollbar.pack(side=RIGHT, fill=BOTH)

    listbox.config(yscrollcommand=scrollbar.set)

    scrollbar.config(command=listbox.yview)
    win.bind('<Escape>', lambda event, a=win:
    close(a))


def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return ("break")
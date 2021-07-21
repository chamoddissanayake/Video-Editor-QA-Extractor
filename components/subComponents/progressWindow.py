import tkinter as tk
from time import sleep
from tkinter import *
from tkinter.ttk import Progressbar, Style

progress = None
frm1 = None
status_label = None
isDeterminate = True
progressIndeterminate = None


def getProgressWindowView(notebook):
    global progress, frm1, status_label, isDeterminate, progressIndeterminate
    frm1 = tk.Frame(notebook)

    status_label = tk.Label(frm1, text="")
    status_label.pack()

    progress = Progressbar(frm1, orient=HORIZONTAL, length=100, mode='determinate')
    progress.pack(fill="x")

    theme = Style()
    theme.theme_use("winnative")
    theme.configure("green.Horizontal.TProgressbar", background="green", size="50")

    progressIndeterminate = Progressbar(frm1, style="green.Horizontal.TProgressbar",
                                        orient="horizontal", mode="indeterminate", length=400)
    progressIndeterminate.pack(fill="x")
    frm1.update()

    hide_indeterminate()

    frm1.pack(side=tk.BOTTOM, anchor=tk.SW, fill="x")

    return frm1


def play_animation():
    for i in range(2000):
        progressIndeterminate['value'] += 1
        frm1.update_idletasks()
        sleep(0.01)
    else:
        frm1.destroy()
        exit(0)


def show_determinate():
    progress.pack(fill="x")


def hide_determinate():
    progress.pack_forget()


def show_indeterminate():
    progressIndeterminate.pack(fill="x")


def hide_indeterminate():
    progressIndeterminate.pack_forget()


def bar(value):
    progress['value'] = value
    frm1.update_idletasks()


def barIndeterminate():
    progressVal = 5

    for i in range(2000):
        progressIndeterminate['value'] += 1
        frm1.update_idletasks()
        sleep(0.01)

    progressIndeterminate['value'] = 0


def chatAndVideoSelectStatus(isVideoSelected, isChatSelected):
    if isVideoSelected == True and isChatSelected == False:
        status_label.config(text="Only Video Imported.")
    elif isVideoSelected == False and isChatSelected == True:
        status_label.config(text="Only Chat File Imported.")
    elif isVideoSelected == True and isChatSelected == True:
        status_label.config(text="Video and Chat File Imported.")
    elif isVideoSelected == False and isChatSelected == False:
        status_label.config(text="None")

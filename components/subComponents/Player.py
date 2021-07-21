import datetime
import os
import time
import tkinter as tk
from tkinter import *
from tkinter import font as tkFont
from tkinter import ttk

import vlc

import utils.constants
from components.subComponents import loginPopup
from utils import constants
from utils import general


instance = None
player = None
isPaused = False
play_pause_btn_label = "⏸"
timeSlider = None
timeSliderLast = 0
timeSliderUpdate = 0
timeVar = 0
nb = None
volMuted = False
_stopped = None
current_play_timestamp = "00:00"
full_video_length = "10:00"
time_label_current = None
time_label_full = None

playing_sentence = ""
logged_in_user_label = None
login_btn = None


def getView(notebook):
    global current_play_timestamp_lbl, play_pause_btn, timeSlider, timeSliderLast, timeSliderUpdate, timeVar, nb, volVar, volMuted, volSlider, \
        mute_button, current_play_timestamp, full_video_length, time_label_current, time_label_full, logged_in_user_label, login_btn
    nb = notebook
    f1 = ttk.Frame(notebook)

    s = ttk.Style()
    s.configure('new.TFrame', background='gray')

    frm1 = ttk.Frame(notebook, style='new.TFrame')
    canvas = tk.Canvas(frm1, width=400, height=150, bg='yellow')
    canvas.pack(side=tk.TOP, anchor=tk.CENTER, padx=5, pady=(5, 100))
    frm1.pack(side=tk.TOP, anchor=tk.NW, padx=20, pady=20)

    global instance, player
    instance = vlc.Instance()
    player = instance.media_player_new()

    utils.constants.main_player = player
    player.video_set_aspect_ratio("16:9")

    if instance is not None:
        play_default_or_selected_video()

    player.set_hwnd(canvas.winfo_id())

    timer_panel = tk.Frame(notebook)
    timer_panel.place(x=32, y=230)

    time_label_current = tk.Label(timer_panel, text=current_play_timestamp)
    time_label_current.pack(side=tk.LEFT)

    time_label_full = tk.Label(timer_panel, text=full_video_length)
    time_label_full.pack(side=tk.RIGHT)

    timers = tk.Frame(timer_panel)
    timeVar = tk.DoubleVar()
    timeSliderLast = 0
    timeSlider = tk.Scale(timers, variable=timeVar, command=OnTime,
                          from_=0, to=1000, orient=tk.HORIZONTAL, length=300,
                          showvalue=0)
    timeSlider.pack(side=tk.BOTTOM, fill=tk.X, expand=1)
    timeSliderUpdate = time.time()
    timers.pack(side=tk.BOTTOM, fill=tk.X)

    current_play_timestamp_lbl = tk.Label(notebook,
                                          text="", wraplength=500, width=100)
    current_play_timestamp_lbl.place(x=500, y=230)

    label = tk.Label(notebook, text='Title:')
    label.place(x=800, y=60)

    sv = tk.StringVar()
    sv.trace("w", lambda name, index, mode, sv=sv: titleTextChangeFunc(sv))
    e = tk.Entry(notebook, textvariable=sv, width=80)
    e.place(x=800, y=80)

    #
    label = tk.Label(notebook, text='By:')
    label.place(x=800, y=100)

    sv = tk.StringVar()
    sv.trace("w", lambda name, index, mode, sv=sv: lecturerTextChangeFunc(sv))
    e = tk.Entry(notebook, textvariable=sv, width=80)
    e.place(x=800, y=120)

    label = tk.Label(notebook, text='Subject:')
    label.place(x=800, y=140)

    logged_in_user_label = tk.Label(notebook, text="")
    logged_in_user_label.place(x=1350, y=50)

    helv11 = tkFont.Font(family='Helvetica', size=11, weight=tkFont.BOLD)

    icon_login = PhotoImage(file=os.path.abspath(os.curdir) + "/assets/icons/buttons/login.png")
    login_btn = tk.Button(notebook, image=icon_login, text=' Login', compound=LEFT, width=70, height=24, relief=FLAT,
                          font=helv11, command=lambda: login_logout_checker())
    login_btn.image = icon_login
    login_btn.place(x=1410, y=45)

    icon_power = PhotoImage(file=os.path.abspath(os.curdir) + "/assets/icons/buttons/power-off.png")
    power_btn = tk.Button(notebook, image=icon_power, text='', compound=LEFT, width=24, height=24, relief=FLAT,
                          font=helv11, command=general.appRestart)
    power_btn.image = icon_power
    power_btn.place(x=1490, y=45)

    var = tk.StringVar()
    options = constants.listOfAvailableSubjects
    var.set(options[0])
    constants.selectedSubjectDropDown = options[0]

    tk.OptionMenu(notebook, var, *(options), command=OptionMenu_SelectionEvent).place(x=800, y=160)

    buttons_panel = tk.Frame(notebook)
    buttons_panel.place(x=60, y=250)

    stop_btn = tk.Button(buttons_panel, text=" 🔁 ", font=30, command=stop)

    play_pause_btn = tk.Button(buttons_panel, text="⏸", font=30, command=play_pause)

    volMuted = False
    mute_button = tk.Button(buttons_panel, text="🔇", font=30, command=OnMute)

    play_pause_btn.pack(side=tk.LEFT, padx=10)
    stop_btn.pack(side=tk.LEFT, padx=10)
    mute_button.pack(side=tk.LEFT, padx=10)

    volVar = tk.IntVar()
    volVar.set(100)
    volSlider = tk.Scale(buttons_panel, variable=volVar, command=OnVolume,
                         from_=0, to=100, orient=tk.HORIZONTAL, length=100,
                         showvalue=100, label='Volume:')
    volSlider.pack(side=tk.RIGHT, padx=10)
    player.audio_set_mute(volMuted)

    OnTick()
    return f1


def login_logout_checker():
    if (constants.loggedInUserID == ""):
        loginPopup.showLogin()
    else:
        # logout
        constants.loggedInUserID = ""
        logged_in_user_label.config(text=constants.loggedInUserID)
        login_btn.config(text=' Login')


def OptionMenu_SelectionEvent(event):
    constants.selectedSubjectDropDown = event
    pass


def play_default_or_selected_video():
    if utils.constants.new_video_import_path != "":
        media = instance.media_new(utils.constants.new_video_import_path)
        player.set_media(media)
        player.play()
    else:
        media = instance.media_new("loading.mp4")
        player.set_media(media)
        player.play()


def play():
    global player
    player.play()


def play_pause():
    global player, play_pause_btn, isPaused
    if isPaused:
        player.play()
        play_pause_btn['text'] = "⏸"
        isPaused = False
    else:
        player.pause()
        play_pause_btn['text'] = " ▶ "
        isPaused = True


def OnTime(self):
    global timeVar, timeSliderLast, timeSliderUpdate
    if player:
        t = timeVar.get()
        if timeSliderLast != int(t):
            player.set_time(int(t * 1e3))  # milliseconds
            timeSliderUpdate = time.time()


def OnTimeChange(sentence_start_time_as_num):
    print(sentence_start_time_as_num)
    global timeVar, timeSliderLast, timeSliderUpdate
    if player:
        print(int(sentence_start_time_as_num) * 1e3)
        player.set_time(int(int(sentence_start_time_as_num) * 1e3))  # milliseconds



def jumpInChat(t):
    global current_play_timestamp_lbl
    from components.subComponents.transcriptWindow import listbox, all_sentence_arr
    index = 0
    for x in all_sentence_arr:
        if x.get_sentenceStartTime() < t:
            index += 1
        else:
            break
    listbox.selection_clear(0, last=listbox.size())
    listbox.selection_set(index - 1)
    if len(all_sentence_arr):
        scrollPercentage = (index - 1) / len(all_sentence_arr)
        listbox.yview_moveto(scrollPercentage)
        current_play_timestamp_lbl.config(text=all_sentence_arr[index - 1].get_sentenceStr())


def OnTick():
    global timeSlider, timeSliderUpdate, timeSliderLast, timeVar, nb, current_play_timestamp, full_video_length
    if player and timeSlider:
        t = player.get_length() * 1e-3

        z = datetime.timedelta(seconds=int(t))
        time_label_full.config(text=str(z))
        if t > 0:
            timeSlider.config(to=t)
            t = player.get_time() * 1e-3
            z = datetime.timedelta(seconds=int(t))
            time_label_current.config(text=str(z))
            if t > 0 and time.time() > (timeSliderUpdate + 2):
                timeSlider.set(t)
                timeSliderLast = int(timeVar.get())
                jumpInChat(t)
    nb.after(500, OnTick)


# t.__str__()

def OnVolume(self):
    global volVar, volMuted, volSlider
    vol = min(volVar.get(), 100)
    v_M = "%s" % (" (Muted)" if volMuted else '')
    volSlider.config()
    if player and not _stopped:
        if player.audio_set_volume(vol):
            print("Failed to set the volume: %s." % (v_M,))


def OnMute():
    global volMuted, mute_button
    volMuted = not volMuted
    player.audio_set_mute(volMuted)
    u = "🔈" if volMuted else "🔇"
    mute_button.config(text=u)
    OnVolume(None)


def stop():
    global timeSlider, play_pause_btn, current_play_timestamp_lbl
    player.stop()
    timeSlider.set(0)
    play_pause_btn.config(text=" ▶ ")
    time_label_current.config(text="00:00:00")
    isPaused = True


def titleTextChangeFunc(sv):
    constants.lecture_name = sv.get()


def lecturerTextChangeFunc(sv):
    constants.lecturer_name = sv.get()

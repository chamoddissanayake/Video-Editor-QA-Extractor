import datetime
import time
import tkinter as tk
from tkinter import ttk

import vlc

instance = None
player1 = None
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

logged_in_user_label = None
login_btn = None


def showAdPopup():
    winShowAd = tk.Toplevel()

    windowWidth = winShowAd.winfo_reqwidth()
    windowHeight = winShowAd.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(winShowAd.winfo_screenwidth() / 4 - windowWidth / 2)
    positionDown = int(winShowAd.winfo_screenheight() / 4 - windowHeight / 2)

    # Positions the window in the center of the page.
    winShowAd.geometry("+{}+{}".format(positionRight, positionDown))
    winShowAd.geometry("1024x576+{}+{}".format(positionRight, positionDown))

    winShowAd.wm_title("Please watch this video while Transcribing. It may Take a while ....")

    getAdPlayerView(winShowAd)

    winShowAd.bind('<Escape>', lambda event, a=winShowAd: close(a))
    winShowAd.bind('<Destroy>', lambda event, a=winShowAd: close(a))
    return winShowAd


def close(winShowAd):
    stopPlayer()
    winShowAd.destroy()


def getAdPlayerView(winShowAd):
    global play_pause_btn, timeSlider, timeSliderLast, timeSliderUpdate, timeVar, nb, volVar, volMuted, volSlider, \
        mute_button, current_play_timestamp, full_video_length, time_label_current, time_label_full, logged_in_user_label, login_btn
    nb = winShowAd
    f1 = ttk.Frame(winShowAd)

    s = ttk.Style()
    s.configure('new.TFrame')

    frm1 = ttk.Frame(winShowAd)
    canvas = tk.Canvas(frm1, width=1280, height=720)
    canvas.pack(side=tk.TOP, anchor=tk.CENTER, padx=5, pady=(5, 100))
    frm1.pack(side=tk.TOP, anchor=tk.NW, padx=20, pady=20)

    global instance, player1
    instance = vlc.Instance()
    player1 = instance.media_player_new()
    player1.video_set_aspect_ratio("16:9")

    if instance is not None:
        play_default_or_selected_video()

    player1.set_hwnd(canvas.winfo_id())

    timer_panel = tk.Frame(winShowAd)
    timer_panel.place(x=32, y=230)

    time_label_current = tk.Label(timer_panel, text=current_play_timestamp)
    time_label_current.pack(side=tk.LEFT)

    time_label_full = tk.Label(timer_panel, text=full_video_length)
    time_label_full.pack(side=tk.RIGHT)

    timers = tk.Frame(timer_panel)
    timeVar = tk.DoubleVar()
    timeSliderLast = 0
    timeSlider = tk.Scale(timers, variable=timeVar, command=OnTime,
                          from_=0, to=1000, orient=tk.HORIZONTAL, length=870,
                          showvalue=0)
    timeSlider.pack(side=tk.BOTTOM, fill=tk.X, expand=1)
    timeSliderUpdate = time.time()
    timers.pack(side=tk.BOTTOM, fill=tk.X)

    timer_panel.place(x=30, y=465)

    buttons_panel = tk.Frame(winShowAd)
    buttons_panel.place(x=330, y=490)

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
    player1.audio_set_mute(volMuted)

    OnTick()
    return f1


def play_default_or_selected_video():
    media = instance.media_new("ad.mp4")
    player1.set_media(media)
    player1.play()


def play():
    global player1
    player1.play()


def play_pause():
    global player1, play_pause_btn, isPaused
    if isPaused:
        player1.play()
        play_pause_btn['text'] = "⏸"
        isPaused = False
    else:
        player1.pause()
        play_pause_btn['text'] = " ▶ "
        isPaused = True


def OnTime(self):
    global timeVar, timeSliderLast, timeSliderUpdate
    if player1:
        t = timeVar.get()
        if timeSliderLast != int(t):
            player1.set_time(int(t * 1e3))  # milliseconds
            timeSliderUpdate = time.time()


def OnTimeChange(sentence_start_time_as_num):
    global timeVar, timeSliderLast, timeSliderUpdate
    if player1:
        player1.set_time(int(int(sentence_start_time_as_num) * 1e3))  # milliseconds


def jumpInChat(t):
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


def OnTick():
    global timeSlider, timeSliderUpdate, timeSliderLast, timeVar, nb, current_play_timestamp, full_video_length
    if player1 and timeSlider:
        t = player1.get_length() * 1e-3

        z = datetime.timedelta(seconds=int(t))
        time_label_full.config(text=str(z))  # t.__str__()
        if t > 0:
            timeSlider.config(to=t)
            t = player1.get_time() * 1e-3
            z = datetime.timedelta(seconds=int(t))
            time_label_current.config(text=str(z))
            if t > 0 and time.time() > (timeSliderUpdate + 2):
                timeSlider.set(t)
                timeSliderLast = int(timeVar.get())
                jumpInChat(t)
    nb.after(500, OnTick)


def OnVolume(self):
    global volVar, volMuted, volSlider
    vol = min(volVar.get(), 100)
    v_M = "%s" % (" (Muted)" if volMuted else '')
    volSlider.config()


def OnMute():
    global volMuted, mute_button
    print(volMuted)
    volMuted = not volMuted
    player1.audio_set_mute(volMuted)
    u = "🔈" if volMuted else "🔇"
    mute_button.config(text=u)
    OnVolume(None)


def stop():
    global timeSlider, play_pause_btn
    print("stop pressed")
    player1.stop()
    timeSlider.set(0)
    play_pause_btn.config(text=" ▶ ")
    time_label_current.config(text="00:00:00")
    isPaused = True


def stopPlayer():
    player1.stop()

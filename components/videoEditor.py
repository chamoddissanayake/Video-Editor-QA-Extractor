from tkinter import *
from tkinter import messagebox
from functions.video_editor.ffmpegEditor import mainAudio
from functions.video_editor.freezScreen import mainVideo


def getView(notebook):

    def AudioEdit_pressed():
        Noise = Noise_entry.get()
        duration = duration_entry.get()

        if Noise == 0 or duration == 0:
            messagebox.showerror("Required inputs", "Please insert a int value")
            return

        mainAudio(threshold=Noise, duration=duration)

    def VideoEdit_pressed():
        Noise = Noise_entry.get()
        duration = duration_entry.get()

        if Noise == 0 or duration == 0:
            messagebox.showerror("Required inputs", "Please insert a int value")
            return

        mainVideo(noise=Noise, duration=duration)

    f1 = Frame(notebook, bg="white")
    f1.pack()

    Decibel_No = StringVar()
    silent_duration = StringVar()

    Noise_label = Label(f1, text="Noise(inDecibel): ")
    Noise_label.grid(row=5, column=5, sticky=W)
    Noise_entry = Entry(f1, textvariable=Decibel_No)
    Noise_entry.grid(row=5, column=6)

    duration_label = Label(f1, text="Silent duration: ")
    duration_label.grid(row=10, column=5, sticky=W)
    duration_entry = Entry(f1, textvariable=silent_duration)
    duration_entry.grid(row=10, column=6)

    button = Button(f1, text="Audio Edit", command=AudioEdit_pressed)
    button.grid(row=15, column=5, sticky=W)

    button = Button(f1, text="Video Edit", command=VideoEdit_pressed)
    button.grid(row=15, column=6, sticky=W)

    return f1

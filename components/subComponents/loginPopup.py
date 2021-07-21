import os
import tkinter as tk
import tkinter.messagebox
from tkinter import *

from utils.aws import loginHandler

global input_username
global input_password


def showLogin():
    global win
    win = tk.Toplevel()

    windowWidth = win.winfo_reqwidth()
    windowHeight = win.winfo_reqheight()

    positionRight = int(win.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(win.winfo_screenheight() / 3 - windowHeight / 2)

    win.geometry("+{}+{}".format(positionRight, positionDown))
    win.geometry("300x400+{}+{}".format(positionRight, positionDown))

    win.wm_title("Login")

    Label(win, text="Login", font=("Arial", 20)).place(x=120, y=30)

    login_photo = PhotoImage(file=os.path.abspath(os.curdir) + "/assets/icons/buttons/login-full.png")
    photo_btn = tk.Button(win, image=login_photo, text='', compound=LEFT, width=100, height=100, relief=FLAT)
    photo_btn.image = login_photo
    photo_btn.place(x=100, y=80)

    Label(win, text="Please login to upload").place(x=95, y=220)

    Label(win, text="Username").place(x=20, y=250)

    Label(win, text="Password").place(x=20, y=290)

    svun = tk.StringVar()
    svun.trace("w", lambda name, index, mode, sv=svun: usernameTextChangeFunc(sv))
    e1 = tk.Entry(win, textvariable=svun, width=30)
    e1.place(x=90, y=250)

    e1.focus()



    svpwd = tk.StringVar()
    svpwd.trace("w", lambda name, index, mode, sv=svpwd: passwordTextChangeFunc(sv))
    e2 = tk.Entry(win, textvariable=svpwd, width=30, show="*")
    e2.place(x=90, y=290)

    e2.bind("<Return>", (lambda event: loginPressed()))
    e1.bind("<Return>", (lambda event: e2.focus()))
    Button(win, text="Login", width=15, height=1, command=loginPressed).place(x=90, y=340)


def usernameTextChangeFunc(sv):
    global input_username
    input_username = sv.get()


def passwordTextChangeFunc(sv):
    global input_password
    input_password = sv.get()


def loginPressed():
    global input_username, input_password, win
    print(input_password)
    print(input_username)

    if input_username == '' and input_password == '':
        tkinter.messagebox.showinfo(title='Error', message='Please enter username and password')
    elif input_username == '':
        tkinter.messagebox.showinfo(title='Error', message='Please enter username')
    elif input_username == '' and input_password == '':
        tkinter.messagebox.showinfo(title='Error', message='Please enter password')
    else:
        loginHandler.validateLoginInAWS_RDS(input_username, input_password, win)

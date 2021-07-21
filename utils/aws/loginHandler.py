import tkinter as tk
import tkinter.messagebox
from tkinter.ttk import Label

import pymysql.cursors

from components.subComponents import Player
from utils import constants
from utils import passwordEncryptor


def validateLoginInAWS_RDS(input_username, input_password, winMain):
    connection = pymysql.connect(host=constants.host,
                                 user=constants.user,
                                 password=constants.password,
                                 database=constants.database,
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `lecturer_credentials` WHERE `lecurerID`=%s"
            cursor.execute(sql, (input_username))
            result = cursor.fetchone()

            if result is None:
                tkinter.messagebox.showinfo(title='Error', message='Incorrect Lecturer ID.')
            else:

                encryptedPasswordFromDB = result.get('encrypted_password')
                encryptedVersionOfInputPassword = passwordEncryptor.getEncryptedPassword(input_password)

                loginSuccess = False
                if encryptedPasswordFromDB.strip() == encryptedVersionOfInputPassword.strip():
                    loginSuccess = True

                if loginSuccess:
                    showLoginSuccess(winMain)
                    constants.isLoggedIn = True
                    constants.loggedInUserID = result.get('lecurerID')
                    Player.logged_in_user_label.config(text=constants.loggedInUserID)
                    Player.login_btn.config(text='Logout')
                else:
                    tkinter.messagebox.showinfo(title='Error', message='Password is incorrect')
                connection.commit()


MSG_DURATION = 2000


def showLoginSuccess(winMain):
    win = tk.Toplevel()

    windowWidth = win.winfo_reqwidth()
    windowHeight = win.winfo_reqheight()

    positionRight = int(win.winfo_screenwidth() / 2 - windowWidth / 5)
    positionDown = int(win.winfo_screenheight() / 3 - windowHeight / 6)

    win.geometry("+{}+{}".format(positionRight, positionDown))
    win.geometry("180x50+{}+{}".format(positionRight, positionDown))

    win.wm_title("Success")

    Label(win, text="Login Success!!!", font=("Arial", 13)).place(x=10, y=10)

    win.after(MSG_DURATION, win.destroy)
    winMain.after(MSG_DURATION, winMain.destroy)

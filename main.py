#!/usr/bin/env python3

from tkinter import Tk

from pages import win_main
# import lib.global_variable as glv
import os

from utils.classifier import modelTrain
import  threading

class App(Tk):
# glv.init_global_variable()
# glv.set_variable("APP_NAME", "Application")
# glv.set_variable("APP_PATH", os.path.dirname(__file__))  # Current directory
    """Application Class"""

    def __init__(self):
        win_main.Main()
        Tk.__init__(self)

        # self.mainloop()


if __name__ == "__main__":
    threading.Thread(target=modelTrain.fileCheckExistSavedData(), daemon=True).start()
    App()

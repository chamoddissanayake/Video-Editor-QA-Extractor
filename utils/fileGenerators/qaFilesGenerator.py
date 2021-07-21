import json
import os
import tkinter.messagebox

from utils import constants


def generateChatQAFile(filename):
    outputchatQAFile = os.path.abspath(os.curdir) + "/tempStorage/generatedFiles/" + "chat-"+filename + '.json'

    with open(outputchatQAFile, 'w') as file:
        json.dump(constants.chat_q_with_a, file)
    tkinter.messagebox.showinfo(title='success', message='Chat QA File saved successfully')

    constants.finalSavedChatQAPath = outputchatQAFile


def generateManualQAFile(filename):
    outputManualQAFile = os.path.abspath(os.curdir) + "/tempStorage/generatedFiles/" + "manual-" + filename + '.json'

    with open(outputManualQAFile, 'w') as file:
        json.dump(constants.manual_q_with_a, file)
    tkinter.messagebox.showinfo(title='success', message='Manual QA File saved successfully')

    constants.finalSavedManualQAPath = outputManualQAFile
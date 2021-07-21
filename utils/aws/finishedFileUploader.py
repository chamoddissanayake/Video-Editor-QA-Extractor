import tkinter.messagebox

from utils import constants
from utils.aws import finishedFilesUploaderImpl


def finishedFileUploaderFunc(filesUploadedLbl):

    if not constants.isLoggedIn:
        tkinter.messagebox.showinfo(title='Error', message='Please Login First')
    else:

        finishedFilesUploaderImpl.uploaderTriggered(filesUploadedLbl)
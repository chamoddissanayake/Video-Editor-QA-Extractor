import threading
import time
import tkinter.messagebox

from components.subComponents import progressWindow
from utils import constants
from utils import value
from utils.fileGenerators import timestampFileGenerator, pdfGenerator, qaFilesGenerator


def fileGenerateMediatorFunc(filesGeneratedLbl):
    threading.Thread(target=fileGeneratorFunc, args=(filesGeneratedLbl,), daemon=True).start()


def fileGeneratorFunc(filesGeneratedLbl):
    if constants.lecture_name == '' or constants.lecturer_name == '':
        tkinter.messagebox.showinfo(title='Error',
                                    message='Please fill Topic of the lecture and the name of the lecturer.')
    else:

        value.program_status = "GENERATING_DOCUMENTS"
        progressWindow.status_label.config(text="Generating Documents")

        progressWindow.hide_determinate()
        progressWindow.show_indeterminate()

        threading.Thread(target=progressTimerFunc, daemon=True).start()

        current_time = int(time.time())
        filename = constants.lecture_name + "-" + constants.lecturer_name + "-" + str(current_time)
        timestampFileGenerator.generateTimestampJson(filename);
        qaFilesGenerator.generateChatQAFile(filename)
        qaFilesGenerator.generateManualQAFile(filename)
        pdfGenerator.generatePDFDocument(filename);

        progressWindow.status_label.config(text="Done")
        progressWindow.hide_indeterminate()
        progressWindow.show_determinate()
        value.program_status = "DOCUMENTS_GENERATED"
        filesGeneratedLbl.set("Files Generated")

    return True


def progressTimerFunc():
    progressWindow.barIndeterminate()
    time.sleep(0.5)
    progressWindow.barIndeterminate()
    time.sleep(0.5)
    progressWindow.barIndeterminate()

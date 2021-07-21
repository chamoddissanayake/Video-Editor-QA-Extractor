import threading
import time
import tkinter.messagebox

from components.subComponents import questionSelectionWindow, progressWindow
from functions.qa import lecturerAnswerProvider
from functions.qa import questionDetector, chatFileReader, findChatAnswersInVideo
from utils import constants
from utils import general
from utils import value
from utils.constants import all_sentences_obj_arr


def questionDetectorAndAnswerHandlerMediator(notebook):
    if constants.hasVideo and len(all_sentences_obj_arr) > 0:
        threading.Thread(target=extractQuestionFunc, daemon=True).start()
    else:
        tkinter.messagebox.showinfo(title='Error', message='Please transcribe first')
        return


def tempQuestionDetectorAndAnswerHandlerMediator(notebook):
    if len(all_sentences_obj_arr) > 0:
        threading.Thread(target=extractQuestionFunc, daemon=True).start()


def extractQuestionFunc():
    value.program_status = "DETECTING_QUESTIONS"

    progressWindow.status_label.config(text="Extracting Questions")

    progressWindow.hide_determinate()
    progressWindow.show_indeterminate()

    threading.Thread(target=progressTimerFunc, daemon=True).start()

    questionDetector.extractQuestionsInVideo(constants.all_sentences_obj_arr)
    lecturerAnswerProvider.checkIfQuestionAskedFromStudentAndLecturerProvidedAnswer();

    if constants.hasChatExport:
        chatfilePath = constants.chat_import_path
        chatArr = chatFileReader.readChatFile(chatfilePath)
        if chatArr is not None:
            questionDetector.questionDetectionFunc(chatArr)

    value.program_status = "QUESTIONS_DETECTED"
    progressWindow.status_label.config(text="Done")
    progressWindow.hide_indeterminate()
    progressWindow.show_determinate()

    findChatAnswersInVideo.findChatAnswersInVideoFunc()

    clean_video_file_question_arr_if_it_contains_duplicated_data_same_as_chat_file_question_arr();
    questionSelectionWindow.extractedQuestionsSelectionPopup()


def progressTimerFunc():
    progressWindow.barIndeterminate()
    time.sleep(0.5)
    progressWindow.barIndeterminate()
    time.sleep(0.5)
    progressWindow.barIndeterminate()


def clean_video_file_question_arr_if_it_contains_duplicated_data_same_as_chat_file_question_arr():
    general.identifyPartsInvideo_file_question_arr()


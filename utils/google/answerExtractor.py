import threading
import time

from components.subComponents import foundAnswersWindow, progressWindow
from utils import constants
from utils import value
from utils.google import answerJsonHandler, relevantAnswerFinder


def findAnswersFromGoogleMediator():
    value.program_status = "FINDING_ANSWERS"
    progressWindow.status_label.config(text="Finding Answers")

    progressWindow.hide_determinate()
    progressWindow.show_indeterminate()

    threading.Thread(target=progressTimerFunc, daemon=True).start()

    video_q_with_a_local = []
    for questionItem in constants.ready_to_find_answers_video_questions:
        if questionItem['checked']:
            # TODO: UNCOMMENT OR COMMENT
            completeResponseJson = answerJsonHandler.getAnswerJsonFunc(questionItem['question'])
            # find the most relevant 3 answers
            relevantIndexArr = relevantAnswerFinder.relevantAnswerFinderFunc(completeResponseJson,
                                                                             questionItem['question'])
            formattedJson = answerJsonHandler.getOnlyRelevantInReceivedJson(completeResponseJson, relevantIndexArr)
            answers = answerJsonHandler.setAnswersFromFormattedJson(formattedJson)

            # answers = [{"a":"found answer from google","cited":"https://google.com"},  {"a":"found answer from google","cited":"https://google.com"},{"a":"found answer from google", "cited":"https://google.com"}]

            currentItem = {
                "question": questionItem['question'],
                "checked": questionItem['checked'],
                "endTime": questionItem['endTime'],
                "google_answer": answers,
                "has_lecturer_answer": questionItem['has_lecturer_answer'],
                "sentence_type": questionItem['sentence_type'],
                "speakerType": questionItem['speakerType'],
                "startTime": questionItem['startTime'],
                "lecturer_answer": questionItem['lecturer_answer'],
                "is_saying_chat_q": questionItem['is_saying_chat_q'],
                "is_saying_chat_str": questionItem['is_saying_chat_str']
            }
            video_q_with_a_local.append(currentItem)
        else:
            currentItem = {
                "question": questionItem['question'],
                "checked": questionItem['checked'],
                "endTime": questionItem['endTime'],
                "google_answer": [],
                "has_lecturer_answer": questionItem['has_lecturer_answer'],
                "sentence_type": questionItem['sentence_type'],
                "speakerType": questionItem['speakerType'],
                "startTime": questionItem['startTime'],
                "lecturer_answer": questionItem['lecturer_answer'],
                "is_saying_chat_q": questionItem['is_saying_chat_q'],
                "is_saying_chat_str": questionItem['is_saying_chat_str']
            }
            video_q_with_a_local.append(currentItem)
    constants.video_q_with_a = video_q_with_a_local

    chat_q_with_a_local = []
    for questionItem in constants.ready_to_find_answers_chat_questions:
        if questionItem['checked']:
            # TODO:UNCOMMENT OR COMMENT
            completeResponseJson = answerJsonHandler.getAnswerJsonFunc(questionItem['question'])
            # find the most relevant 3 answers
            print("<--" + questionItem['question'] + "-->")
            relevantIndexArr = relevantAnswerFinder.relevantAnswerFinderFunc(completeResponseJson,
                                                                             questionItem['question'])
            formattedJson = answerJsonHandler.getOnlyRelevantInReceivedJson(completeResponseJson, relevantIndexArr)
            answers = answerJsonHandler.setAnswersFromFormattedJson(formattedJson)

            # answers = [{"a":"found answer from google","cited":"https://google.com"},  {"a":"found answer from google","cited":"https://google.com"},{"a":"found answer from google", "cited":"https://google.com"}]

            currentItem = {
                "question": questionItem['question'],
                "has_lecturer_answer": questionItem['has_lecturer_answer'],
                "question_type": questionItem['question_type'],
                "receiver": questionItem['receiver'],
                "sender": questionItem['sender'],
                "lecturer_answer": questionItem['lecturer_answer'],
                "timestamp": questionItem['timestamp'],
                "checked": questionItem['checked'],
                "google_answer": answers
            }
            chat_q_with_a_local.append(currentItem)
        else:
            currentItem = {
                "question": questionItem['question'],
                "has_lecturer_answer": questionItem['has_lecturer_answer'],
                "question_type": questionItem['question_type'],
                "receiver": questionItem['receiver'],
                "sender": questionItem['sender'],
                "lecturer_answer": questionItem['lecturer_answer'],
                "timestamp": questionItem['timestamp'],
                "checked": questionItem['checked'],
                "google_answer": []
            }
            chat_q_with_a_local.append(currentItem)
    constants.chat_q_with_a = chat_q_with_a_local

    manual_q_with_a_local = []
    for questionItem in constants.ready_to_find_answers_manual_questions:
        # TODO: UNCOMMENT
        completeResponseJson = answerJsonHandler.getAnswerJsonFunc(questionItem['question'])
        # find the most relevant 3 answers
        print("<--" + questionItem['question'] + "-->")
        relevantIndexArr = relevantAnswerFinder.relevantAnswerFinderFunc(completeResponseJson, questionItem['question'])
        formattedJson = answerJsonHandler.getOnlyRelevantInReceivedJson(completeResponseJson, relevantIndexArr)
        answers = answerJsonHandler.setAnswersFromFormattedJson(formattedJson)
        # answers = [{"a": "found answer from google", "cited": "https://google.com"},
        #            {"a": "found answer from google", "cited": "https://google.com"},
        #            {"a": "found answer from google", "cited": "https://google.com"}]

        currentItem = {
            "question": questionItem['question'],
            "lecturer_answer": questionItem['lecturer_answer'],
            "google_answer": answers,
            "checked": questionItem['checked'],
        }
        manual_q_with_a_local.append(currentItem)
    constants.manual_q_with_a = manual_q_with_a_local

    value.program_status = "ANSWERS_FOUND"

    progressWindow.status_label.config(text="Answers Found")
    progressWindow.hide_indeterminate()
    progressWindow.show_determinate()

    foundAnswersWindow.showFoundAnswersWindow()

    return True


def progressTimerFunc():
    progressWindow.barIndeterminate()
    time.sleep(0.5)
    progressWindow.barIndeterminate()
    time.sleep(0.5)
    progressWindow.barIndeterminate()

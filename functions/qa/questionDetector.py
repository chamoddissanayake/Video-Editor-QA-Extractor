from functions.qa import interrogativeDetector, domainNonDomainQuestionClassifier
from utils import constants


def questionDetectionFunc(chatArr):

    interrogativeDetector.identify_interrogative_or_not(chatArr, 'Chat')
    domainNonDomainQuestionClassifier.domainNonDomainQuestionClassifierFunc(constants.chat_file_question_arr, 'Chat')


def extractQuestionsInVideo(all_sentences_obj_arr):
    interrogativeDetector.identify_interrogative_or_not(all_sentences_obj_arr, 'Video')
    domainNonDomainQuestionClassifier.domainNonDomainQuestionClassifierFunc(constants.video_file_question_arr, 'Video')


    return None
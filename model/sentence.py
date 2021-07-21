class Sentence:

    def __init__(self, sentenceStr, sentenceStartTime, sentenceEndTime, sentenceSpeakerType):
        self.__sentenceStr = sentenceStr
        self.__sentenceStartTime = sentenceStartTime
        self.__sentenceEndTime = sentenceEndTime
        self.__sentenceSpeakerType = sentenceSpeakerType

    def get_sentenceStr(self):
        return self.__sentenceStr

    def set_sentenceStr(self, sentenceStr):
        self.__sentenceStr = sentenceStr

    def get_sentenceStartTime(self):
        return self.__sentenceStartTime

    def set_sentenceStartTime(self, sentenceStartTime):
        self.__sentenceStartTime = sentenceStartTime

    def get_sentenceEndTime(self):
        return self.__sentenceEndTime

    def set_sentenceEndTime(self, sentenceEndTime):
        self.__sentenceEndTime = sentenceEndTime

    def get_sentenceSpeakerType(self):
        return self.__sentenceSpeakerType

    def set_sentenceSpeakerType(self, sentenceSpeakerType):
        self.__sentenceSpeakerType = sentenceSpeakerType

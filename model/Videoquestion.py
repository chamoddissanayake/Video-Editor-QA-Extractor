class Videoquestion:

    def __init__(self, startTime, endTime, speakerType, question, sentence_type, has_lecturer_answer, lecturer_answer, google_answer, is_saying_chat_q, is_saying_chat_str):
        self.startTime = startTime
        self.endTime = endTime
        self.speakerType = speakerType
        self.question = question
        self.sentence_type = sentence_type
        self.has_lecturer_answer = has_lecturer_answer
        self.lecturer_answer = lecturer_answer
        self.google_answer = google_answer
        self.is_saying_chat_q = is_saying_chat_q
        self.is_saying_chat_str = is_saying_chat_str

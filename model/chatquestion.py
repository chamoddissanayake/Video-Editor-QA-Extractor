class Chatquestion:

    def __init__(self, timestamp,sender,receiver,question,question_type,has_lecturer_answer,lecturer_answer,google_answer ):
        self.timestamp = timestamp
        self.sender = sender
        self.receiver = receiver
        self.question = question
        self.question_type = question_type
        self.has_lecturer_answer = has_lecturer_answer
        self.lecturer_answer = lecturer_answer
        self.google_answer = google_answer

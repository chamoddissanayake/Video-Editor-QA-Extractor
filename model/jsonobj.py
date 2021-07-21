class JSONObj:

    def __init__(self, index,start_timestamp,end_timestamp,speaker,is_question,google_answer,lecturer_answer, has_lecturer_answer,sentence_str ):
        self.index = index
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp
        self.speaker = speaker
        self.is_question = is_question
        self.google_answer = google_answer
        self.lecturer_answer = lecturer_answer
        self.has_lecturer_answer =has_lecturer_answer
        self.sentence_str = sentence_str
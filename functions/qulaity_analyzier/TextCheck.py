import pytesseract

"""
Author: Bandara A.B.C.N
Student ID: IT18117356
Group ID: 2021-064
"""


class TextCheck:
    def __init__(self):
        self.frames = []

    def execute(self, count, frame):
        """
        Args:
            count: count of current iteration in the main loop
            frame: the frame of the current iteration
        Returns:None
        """
        # read text from the frame
        text = pytesseract.image_to_string(frame, lang="eng")

        # get text line in the frame without empty lines.
        arr = [i for i in text.split("\n") if i != ""]

        # if text lines are over 12 then count value saved in the textlines array
        if len(arr) > 12:
            self.frames.append(count)

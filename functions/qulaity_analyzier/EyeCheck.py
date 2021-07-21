import cv2

"""
Author: Bandara A.B.C.N
Student ID: IT18117356
Group ID: 2021-064
"""


class EyeCheck:
    __eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

    def __init__(self):
        self.frames = []

    def execute(self, count, gray_frame, faces):
        """
        Args:
            count: count of current iteration in the main loop
            gray_frame: gray colored frame that was converted from EyeCheck execute method
            faces: faces that was analyzed from EyeCheck execute method
        Returns: None
        """
        for (x, y, w, h) in faces:

            # identify positions.
            roi_gray = gray_frame[y:y + h, x:x + w]

            # identify eyes and assign them into a variable.
            eyes = self.__eye_cascade.detectMultiScale(roi_gray)

            # if there is no eyes then append the count to the frames list.
            if len(eyes) == 0:
                self.frames.append(count)

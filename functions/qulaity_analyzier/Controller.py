import cv2

from functions.qulaity_analyzier.EyeCheck import EyeCheck
from functions.qulaity_analyzier.FaceCheck import FaceCheck
from functions.qulaity_analyzier.PeriodCheck import PeriodCheck
from functions.qulaity_analyzier.TextCheck import TextCheck

"""
Author: Bandara A.B.C.N
Student ID: IT18117356
Group ID: 2021-064
"""


class Controller:

    def __init__(self, period, eye_feature, text_feature, face_feature):
        """
        Args:
            period: minimum time period that should be remove
            eye_feature: availability of eye checking feature
            text_feature: availability of text lines checking feature
            face_feature: availability of face checking feature
        """
        self.__period = period

        # if features are available then creates objects
        self.__eye_check = EyeCheck() if eye_feature else None
        self.__face_check = FaceCheck(self.__eye_check) if face_feature or eye_feature else None
        self.__text_check = TextCheck() if text_feature else None

    def execute(self):
        """
            Returns:A dictionary that has all the time periods that need to be removed
        """
        # get the video
        video = cv2.VideoCapture(
            "/Users/chirannuwan/Downloads/NGINX Explained in 100 Seconds.mp4")

        # if new_video_import_path == "":
        #     messagebox.showerror("Required fields", "Please enter video")
        #
        # video = cv2.VideoCapture(new_video_import_path)

        # get the fps of the video and convert into int
        fps = int(video.get(cv2.CAP_PROP_FPS))

        count = 0

        face = True

        # infinity loop
        while True:
            _, frame = video.read()

            # break the loop if there are no frames
            if frame is None:
                break
            # if users face is not available for 5 minutes then terminate face and eye checking
            if count == fps * 60 * 5:
                if len(self.__face_check.frames) == count:
                    face = False

            # increment the count
            count += 1

            # if the face checking feature and the face is available then execute face and eye checking
            if self.__face_check and face:
                self.__face_check.execute(count, frame)

            # if text lines checking feature is available then execute the text checking
            if self.__text_check:
                self.__text_check.execute(count, frame)

        # release the video after analyze is done
        video.release()

        result = {}

        # set the value to result dictionary
        if self.__face_check:
            no_face = PeriodCheck(self.__face_check.frames, self.__period * fps)
            result["no_faces"] = no_face.periods(fps)
        if self.__eye_check:
            no_eyes = PeriodCheck(self.__eye_check.frames, self.__period * fps)
            result["no_eyes"] = no_eyes.periods(fps)
        if self.__text_check:
            text_line = PeriodCheck(self.__text_check.frames, 1 * fps)
            result["text_lines"] = text_line.periods(fps)

        return result

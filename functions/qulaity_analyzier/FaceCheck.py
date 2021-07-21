import cv2

"""
Author: Bandara A.B.C.N
Student ID: IT18117356
Group ID: 2021-064
"""
class FaceCheck:
    __face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

    def __init__(self, eye_check_object):
        """
        Args:
            eye_check_object: EyeCheck object
        """
        self.frames = []
        self.__eyeObj = eye_check_object

    def execute(self, count, frame):
        """
        Args:
            count: count of current iteration in the main loop
            frame: the frame of the current iteration
        Returns:None
        """

        # convert the frame into gray color.
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # analyze the frame, get faces from the frame and assign to the variable.
        faces = self.__face_cascade.detectMultiScale(gray_frame, 1.4, 5)

        # if no faces then append that frame into the frames list
        if len(faces) == 0:
            self.frames.append(count)

        # if there are any faces then check EyeCheck object is available.
        else:
            # if eye checking feature is available then execute the eye checking
            if self.__eyeObj:
                self.__eyeObj.execute(count, gray_frame, faces)

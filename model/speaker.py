class Speaker:
    def __init__(self):
        self.lecturerCount = 0
        self.studentCount = 0

    def increaseLecturerCount(self):
        self.lecturerCount += 1

    def increaseStudentCount(self):
        self.studentCount += 1

    def ifLecturer(self):
        if self.lecturerCount > self.studentCount:
            return True
        else:
            return False
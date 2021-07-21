import tkinter.messagebox
from datetime import datetime

import pymysql.cursors

from utils import constants


def insertRecordToStudentTableInRDS():
    connection = pymysql.connect(host=constants.host,
                                 user=constants.user,
                                 password=constants.password,
                                 database=constants.database,
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection:
        with connection.cursor() as cursor:
            subId = ""
            for i in range(7):
                subId = subId + constants.selectedSubjectDropDown[i]

            uploadedBy = constants.loggedInUserID
            title = constants.lecture_name
            lecturerDisplay = constants.lecturer_name
            uploadedTimestamp = datetime.now()
            subject = subId
            videoPath = constants.uploadedS3VideoPath
            documentPath = constants.uploadedS3DocumentPath
            logPath = constants.uploadedS3TimestampFilePath
            chatQAPath = constants.uploadedS3ChatQAFilePath
            manualQAFilePath = constants.uploadedS3ManualQAFilePath
            thumbnailFilePath = constants.uploadedS3ThumbnailPath

            sql = "INSERT INTO `video` (`uploaded_by`, `title` ,`lecturer_display` ,`uploaded_timestamp`, `subject` , `video_path` , `document_path`, `log_path`,`chat_qa_file_path`,`manual_qa_file_path`,`thumbnail_file_path`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); "
            result = cursor.execute(sql, (
                uploadedBy, title, lecturerDisplay, uploadedTimestamp, subject, videoPath, documentPath, logPath,
                chatQAPath, manualQAFilePath, thumbnailFilePath))

            tkinter.messagebox.showinfo(title='Success', message='Successfully Inserted Record')

            connection.commit()

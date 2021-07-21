import os
import sys
import threading

import boto3

from components.subComponents import progressWindow
from utils import constants
from utils import value
from utils.aws import rds


class ProgressPercentage(object):

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write("\r%s  %s / %s  (%.2f%%)" % (self._filename, self._seen_so_far, self._size, percentage))
            progressWindow.bar(percentage)
            sys.stdout.flush()


def uploaderTriggered(filesUploadedLbl):
    threading.Thread(target=finishedFilesUploaderFunc, args=(filesUploadedLbl,), daemon=True).start()


def finishedFilesUploaderFunc(filesUploadedLbl):
    tempVidPath = constants.new_video_import_path
    tempTranscriptPath = constants.finalSavedJsonPath
    tempDocPath = constants.finalSavedDocumentPath
    tempChatFilePath = constants.finalSavedChatQAPath
    tempManualPath = constants.finalSavedManualQAPath
    tempThumbnailPath = constants.thumbnail_path

    filename = os.path.basename(tempTranscriptPath).split('.')[0]

    uploadVideo(tempVidPath, filename)
    uploadTranscriptFile(tempTranscriptPath)
    uploadChatQAFile(tempChatFilePath)
    uploadManualQAFile(tempManualPath)
    uploadPDFdocument(tempDocPath)
    uploadThumbnail(tempThumbnailPath, filename)

    rds.insertRecordToStudentTableInRDS();

    progressWindow.status_label.config(text="Done")
    value.program_status = 'DONE'
    filesUploadedLbl.set("Done")


def uploadVideo(videoFilePath, filename):
    value.program_status = 'VIDEO_UPLOADING'
    progressWindow.bar(0)
    progressWindow.status_label.config(text="Video Uploading. Please wait...")

    new_file_name = filename + "." + os.path.split(videoFilePath)[1].split('.')[1]
    bucket = 'research-project-sliit'
    region = 'ap-south-1'
    folder = 'uploads/videos/'

    s3 = boto3.client('s3')
    with open(videoFilePath, "rb") as f:
        s3.upload_file(
            videoFilePath, bucket, folder + '' + new_file_name,
            Callback=ProgressPercentage(videoFilePath)
        )

        url = f"https://{bucket}.s3.{region}.amazonaws.com/{folder}{new_file_name}"
        value.program_status = 'VIDEO_UPLOADED'
        progressWindow.bar(0)
        progressWindow.status_label.config(text="Video Uploaded")
        constants.uploadedS3VideoPath = url

def uploadTranscriptFile(TranscriptFilePath):
    value.program_status = 'TRANSCRIPT_UPLOADING'
    progressWindow.bar(0)
    progressWindow.status_label.config(text="Transcript File Uploading. Please wait...")

    file_name = os.path.split(TranscriptFilePath)[1]
    bucket = 'research-project-sliit'
    region = 'ap-south-1'
    folder = 'uploads/transcript/'

    s3 = boto3.client('s3')
    with open(TranscriptFilePath, "rb") as f:
        s3.upload_file(
            TranscriptFilePath, bucket, folder + '' + file_name,
            Callback=ProgressPercentage(TranscriptFilePath)
        )

        value.program_status = 'TRANSCRIPT_UPLOADED'
        progressWindow.bar(0)
        progressWindow.status_label.config(text="Transcript File Uploaded")

        url = f"https://{bucket}.s3.{region}.amazonaws.com/{folder}{file_name}"
        constants.uploadedS3TimestampFilePath = url


def uploadPDFdocument(pdfDocumentFilePath):
    value.program_status = 'DOCUMENT_UPLOADING'
    progressWindow.bar(0)
    progressWindow.status_label.config(text="Document Uploading. Please wait...")

    file_name = os.path.split(pdfDocumentFilePath)[1]
    bucket = 'research-project-sliit'
    region = 'ap-south-1'
    folder = 'uploads/documents/'

    s3 = boto3.client('s3')
    with open(pdfDocumentFilePath, "rb") as f:
        s3.upload_file(
            pdfDocumentFilePath, bucket, folder + '' + file_name,
            Callback=ProgressPercentage(pdfDocumentFilePath)
        )

        value.program_status = 'DOCUMENT_UPLOADED'
        progressWindow.bar(0)
        progressWindow.status_label.config(text="Document Uploaded")

        url = f"https://{bucket}.s3.{region}.amazonaws.com/{folder}{file_name}"

        constants.uploadedS3DocumentPath = url


def uploadChatQAFile(ChatQAFilePath):
    value.program_status = 'CHAT_QA_UPLOADING'
    progressWindow.bar(0)
    progressWindow.status_label.config(text="Chat QA File Uploading. Please wait...")

    file_name = os.path.split(ChatQAFilePath)[1]
    bucket = 'research-project-sliit'
    region = 'ap-south-1'
    folder = 'uploads/chat/'

    s3 = boto3.client('s3')
    with open(ChatQAFilePath, "rb") as f:
        s3.upload_file(
            ChatQAFilePath, bucket, folder + '' + file_name,
            Callback=ProgressPercentage(ChatQAFilePath)
        )

        value.program_status = 'CHAT_QA_UPLOADED'
        progressWindow.bar(0)
        progressWindow.status_label.config(text="Chat QA File Uploaded")
        url = f"https://{bucket}.s3.{region}.amazonaws.com/{folder}{file_name}"
        constants.uploadedS3ChatQAFilePath = url


def uploadManualQAFile(ManualQAFilePath):
    value.program_status = 'MANUAL_QA_UPLOADING'
    progressWindow.bar(0)
    progressWindow.status_label.config(text="Manual QA File Uploading. Please wait...")

    file_name = os.path.split(ManualQAFilePath)[1]
    bucket = 'research-project-sliit'
    region = 'ap-south-1'
    folder = 'uploads/manual/'

    s3 = boto3.client('s3')
    with open(ManualQAFilePath, "rb") as f:
        s3.upload_file(
            ManualQAFilePath, bucket, folder + '' + file_name,
            Callback=ProgressPercentage(ManualQAFilePath)
        )

        value.program_status = 'MANUAL_QA_UPLOADED'
        progressWindow.bar(0)
        progressWindow.status_label.config(text="Manual QA File Uploaded")
        url = f"https://{bucket}.s3.{region}.amazonaws.com/{folder}{file_name}"
        constants.uploadedS3ManualQAFilePath = url


def uploadThumbnail(tempThumbnailPath, filename):
    value.program_status = 'THUMBNAIL_UPLOADING'
    progressWindow.bar(0)
    progressWindow.status_label.config(text="Thumbnail is Uploading. Please wait...")

    file_name = filename + "." + os.path.split(tempThumbnailPath)[1].split('.')[1]
    bucket = 'research-project-sliit'
    region = 'ap-south-1'
    folder = 'uploads/thumbnail/'

    s3 = boto3.client('s3')
    with open(tempThumbnailPath, "rb") as f:
        s3.upload_file(
            tempThumbnailPath, bucket, folder + '' + file_name,
            Callback=ProgressPercentage(tempThumbnailPath)
        )

        value.program_status = 'THUMBNAIL_UPLOADED'
        progressWindow.bar(0)
        progressWindow.status_label.config(text="Thumbnail Uploaded")
        url = f"https://{bucket}.s3.{region}.amazonaws.com/{folder}{file_name}"
        constants.uploadedS3ThumbnailPath = url

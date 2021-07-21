new_video_import_path = ""
chat_import_path = ""
converted_audio_path = ""
uploaded_audio_s3_path = ""
current_time = ""

all_sentences_obj_arr = []


hasVideo = False
hasChatExport = False

chat_file_question_arr = []
video_file_question_arr = []
manually_added_question_arr = []

removed_questions_from_video_due_to_answers_already_available_in_chat_section = []


q_list_vid = None
q_list_chat = []
q_list_manual = []

lecture_name = ""
lecturer_name = ""

manual_q_with_a = []
chat_q_with_a = []
video_q_with_a = []

ready_to_find_answers_video_questions = []
ready_to_find_answers_chat_questions = []
ready_to_find_answers_manual_questions = []


google_search_api_key= "AIzaSyAAYO0MQdlB-Uv87JQS5qdauHgJq5ulu5I"


finalSavedJsonPath = ""
finalSavedDocumentPath = ""
finalSavedChatQAPath = ""
finalSavedManualQAPath = ""

host='lmsdb.c0s3dmy3kgif.ap-south-1.rds.amazonaws.com'
user='admin'
password='admin123'
database='lmsDB'

isLoggedIn = False
loggedInUserID = ""


uploadedS3VideoPath=""
uploadedS3DocumentPath=""
uploadedS3TimestampFilePath=""

uploadedS3ChatQAFilePath=""
uploadedS3ManualQAFilePath=""

thumbnail_path = ""
uploadedS3ThumbnailPath=""

selectedSubjectDropDown=""


listOfAvailableSubjects = ["IT 1010  Introduction to Programming",
                "IT 1020  Introduction to Computer Systems",
                "IT 1030  Mathematics for Computing",
                "IT 1040  Communication Skills",
                "IT 1050  Object Oriented Concepts",
                "IT 1060  Software Process Modeling",
                "IT 1080  English for Academic Purposes",
                "IT 1090  Information Systems and Data Modeling",
                "IT 1100  Internet and Web Technologies",
                "IT 2020  Software Engineering",
                "IT 2030  Object Oriented Programming",
                "IT 2040  Database Management Systems",
                "IT 2050  Computer Networks",
                "IT 2060  Operating Systems and System Administration",
                "IT 2010  Mobile Application Development",
                "IT 2070  Data Structures and Algorithms",
                "IT 2080  IT Project",
                "IT 2090  Professional Skills",
                "IT 2110  Probability and Statistics",
                "IT 2100  Employability Skills Development –Seminar",
                "SE 3010  Software Engineering Process & Quality Management",
                "SE 3020  Distributed Systems",
                "SE 3030  Software Architecture",
                "SE 3040  Application Frameworks",
                "IT 3050  Employability Skills Development – Seminar",
                "SE 3050  User Experience Engineering",
                "SE 3060  Database Systems",
                "SE 3070  Case Studies in Software Engineering",
                "SE 3080  Software Project Management",
                "IT 3100  Industry Placement",
                "IT 4010  Research Project",
                "IT 4070  Preparation for the Professional World",
                "SE 4010  Current Trends in Software Engineering",
                "SE 4030  Secure Software Development",
                "IT 4130  Image Understanding & Processing",
                "IT 4060  Machine Learning",
                "SE 4040  Enterprise Application Development",
                "SE 4020  Mobile Application Design & Development",
                "SE 4050  Deep Learning",
                "SE 4060  Parallel Computing",
                "IE 4060  Robotics and Intelligent Systems"]


# Constants for Voice Enhancer
from pathlib import Path

audio_transcription_file_name=''
PROJECT_ROOT = Path(__file__).parent.parent

qa_window_title_color= "#ffd8d8" #pink
qa_window_question_color= "#d8dfff" # light blue
qa_window_lecturer_answer_color= "#ffffbe" # light yellow
qa_window_google_answer_color= "#e9fffd" #light blue
qa_window_empty_line_color= "#eeeeee" #gray


fuzzRatioCutPoint = 90

main_player=None;
import tkinter as tk

from components.subComponents import transcriptWindow, extractedQuestionsAnswersWindow


def getView(notebook):
    f1 = tk.Frame(notebook, bg="old lace")

    transcriptWindow.getTranscribeWindowView(f1)

    extractedQuestionsAnswersWindow.getExtractedQuestionsAndAnswersWindow(f1);

    return f1

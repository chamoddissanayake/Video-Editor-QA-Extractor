from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functions.qulaity_analyzier.Controller import Controller

"""
Author: Bandara A.B.C.N
Student ID: IT18117356
Group ID: 2021-064
"""


class ViewController:
    def __init__(self, frame):
        self.__frame = frame
        self.__table = self.__tree_view()

    def __tree_view(self):

        tree_view = ttk.Treeview(self.__frame)
        tree_view['columns'] = ("Period", "Reason")

        tree_view.column('#0', width=5)
        tree_view.column('Period', anchor=W, width=200)
        tree_view.column('Reason', anchor=W, width=400)

        tree_view.heading('#0', text="No")
        tree_view.heading('Period', text="Period", anchor=W)
        tree_view.heading('Reason', text="Reason", anchor=W)

        tree_view.grid(row=0, column=2, columnspan=2, rowspan=6, pady=20, padx=20)

        return tree_view

    def __validate(self, period, face, eye, text):
        if period == '':
            messagebox.showerror("Required fields", "Please enter the time period that you want to select")
            return

        if eye == 0 and face == 0 and text == 0:
            messagebox.showerror("Required fields", "Please select at least one checkbox")
            return

    def analyze_pressed(self, period, eye, face, text):

        # validate inputs
        self.__validate(period, face, eye, text)

        # get output from the controller
        quality_analyzing_controller = Controller(period=int(period), eye_feature=eye, face_feature=face,
                                                  text_feature=text)

        result = quality_analyzing_controller.execute()

        # get a tree view
        table = self.__table

        count = 0

        # show output
        if face == 1:
            for row in result["no_faces"]:
                count += 1
                table.insert(parent='', index='end', iid=count,
                             values=("From: " + row[0] + " To: " + row[1], "Face could not identified"))

        if eye == 1:
            for row in result["no_eyes"]:
                count += 1
                table.insert(parent='', index='end', iid=count,
                             values=("From: " + row[0] + " To: " + row[1], "Eyes could not identified"))

        if text == 1:
            for row in result["text_lines"]:
                count += 1
                table.insert(parent='', index='end', iid=count,
                             values=(
                                 "From: " + row[0] + " To: " + row[1], "Number of text lines are over twelve lines."))


def getView(notebook):
    f1 = Frame(notebook, bg="old lace")
    f1.pack()

    view_controller = ViewController(f1)

    time_period = StringVar()
    # period label and input field
    period_label = Label(f1, text="Time period(Seconds): ", bg="old lace")
    period_label.grid(row=0, column=0, sticky=W)
    period_entry = Entry(f1, textvariable=time_period)
    period_entry.grid(row=0, column=1)

    # feature label and check boxes
    period_label = Label(f1, text="Features: ", bg="old lace")
    period_label.grid(row=1, column=0, sticky=W)

    eye_feature = IntVar()
    Checkbutton(f1, text="Eye Checking", variable=eye_feature, bg="old lace").grid(row=1, column=1, sticky=W)

    face_feature = IntVar()
    Checkbutton(f1, text="Face Checking", variable=face_feature, bg="old lace").grid(row=2, column=1, sticky=W)

    text_feature = IntVar()
    Checkbutton(f1, text="Text Lines Checking", variable=text_feature, bg="old lace").grid(row=3, column=1, sticky=W)

    # analyze button
    button = Button(f1, text="Analyse",
                    command=lambda: view_controller.analyze_pressed(period_entry.get(), eye_feature.get(),
                                                                    face_feature.get(),
                                                                    text_feature.get()))
    button.grid(row=4, column=1, sticky=W)

    return f1

import os
import tkinter.messagebox
from datetime import datetime

from fpdf import FPDF

from utils import constants


class PDF(FPDF):
    def header(self):
        self.image(os.path.abspath(os.curdir) + "/assets/pdfImg/sliit_logo.png", 95, 8, 25)
        self.set_font('helvetica', 'B', 15)

        self.ln(35)
        self.cell(80)
        self.cell(30, 10, constants.lecture_name, ln=1, align='C')

        self.ln(2)
        self.cell(80)
        self.cell(30, 10, 'By ' + constants.lecturer_name, ln=1, align='C')  # border=True,

        self.ln(0)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.cell(45)
        self.cell(30, 10, 'File Generated on:  ' + dt_string, ln=1)  # border=True,
        self.ln(2)

        self.line(10, 77, 210 - 10, 77);
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 10)
        self.cell(0, 10, f'Page{self.page_no()}/{{nb}}', align='C')


def generatePDFDocument(filename):
    redColor = 0
    greenColor = 0
    blueColor = 200

    pdf = PDF('P', 'mm', 'Letter')

    effective_page_width = pdf.w - 2 * pdf.l_margin


    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_page()


    # Video Q with A
    pdf.set_font('times', 'B', 16)
    topic_vid = "Answers for Questions in Lecture video".encode('latin-1', 'replace').decode('latin-1')
    pdf.cell(0, 10, topic_vid, ln=True, align='C')
    pdf.ln(3)

    pdf.set_font('times', '', 12)

    for item in constants.video_q_with_a:

        pdf.set_font('times', 'B', 14)
        q = "Question:".encode('latin-1', 'replace').decode('latin-1')
        qa = item['question'].encode('latin-1', 'replace').decode('latin-1')

        pdf.multi_cell(effective_page_width / 1.5, 5, q)
        pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)
        pdf.multi_cell(effective_page_width / 1.5, 5, qa)
        pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)

        if item['has_lecturer_answer']:
            pdf.set_font('times', 'B', 12)
            pdf.set_text_color(0, 0, 0)
            qtaTitle = ("     Lecturer Answer:").encode('latin-1', 'replace').decode('latin-1')

            pdf.multi_cell(effective_page_width / 1, 5, qtaTitle)
            pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)
            pdf.set_text_color(0, 0, 0)

            pdf.set_font('times', '', 12)
            pdf.set_text_color(153, 0, 76)
            qta = (item['lecturer_answer']).encode('latin-1', 'replace').decode('latin-1')

            pdf.multi_cell(effective_page_width / 1, 5, qta)
            pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)
            pdf.set_text_color(0, 0, 0)

        if len(item['google_answer']) > 0:
            pdf.set_font('times', 'B', 12)
            pdf.set_text_color(0, 0, 0)
            qqga = ("     Google Answers").encode('latin-1', 'replace').decode('latin-1')
            pdf.multi_cell(effective_page_width / 1, 5, qqga)
            pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)

        for ans in item['google_answer']:
            pdf.set_font('times', '', 12)

            qq1 = ("Answer:    " + ans['a']).encode('latin-1', 'replace').decode('latin-1')
            qqa = ("Reference: " + ans['cited']).encode('latin-1', 'replace').decode('latin-1')

            pdf.multi_cell(effective_page_width / 1, 5, qq1)
            pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)

            pdf.set_text_color(redColor, greenColor, blueColor)
            pdf.multi_cell(effective_page_width / 1, 5, qqa)
            pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)
            pdf.set_text_color(0, 0, 0)

        pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)

        # Chat Q with A
    pdf.cell(ln=1, h=20.0, align='L', w=0, txt="", border=0)
    pdf.set_font('times', 'B', 16)
    topic_chat = "Answers for Chat Questions".encode('latin-1', 'replace').decode('latin-1')
    pdf.cell(0, 10, topic_chat, ln=True, align='C')
    pdf.ln(3)

    pdf.set_font('times', '', 12)

    for item in constants.chat_q_with_a:

        pdf.set_font('times', 'B', 14)
        q = "Question:".encode('latin-1', 'replace').decode('latin-1')
        qa = item['question'].encode('latin-1', 'replace').decode('latin-1')

        pdf.multi_cell(effective_page_width / 1.5, 5, q)
        pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)
        pdf.multi_cell(effective_page_width / 1.5, 5, qa)
        pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)

        if item['has_lecturer_answer']:
            pdf.set_font('times', 'B', 12)
            pdf.set_text_color(0, 0, 0)
            qtaTitle = ("     Lecturer Answer:").encode('latin-1', 'replace').decode('latin-1')

            pdf.multi_cell(effective_page_width / 1, 5, qtaTitle)
            pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)
            pdf.set_text_color(0, 0, 0)

            pdf.set_font('times', '', 12)
            pdf.set_text_color(153, 0, 76)
            qta = (item['lecturer_answer']).encode('latin-1', 'replace').decode('latin-1')

            pdf.multi_cell(effective_page_width / 1, 5, qta)
            pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)
            pdf.set_text_color(0, 0, 0)

        if len(item['google_answer']) > 0:
            pdf.set_font('times', 'B', 12)
            pdf.set_text_color(0, 0, 0)
            qqga = ("     Google Answers").encode('latin-1', 'replace').decode('latin-1')
            pdf.multi_cell(effective_page_width / 1, 5, qqga)
            pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)

        for ans in item['google_answer']:
            pdf.set_font('times', '', 12)
            qq1 = ("Answer:    " + ans['a']).encode('latin-1', 'replace').decode('latin-1')
            qqa = ("Reference: " + ans['cited']).encode('latin-1', 'replace').decode('latin-1')

            pdf.multi_cell(effective_page_width / 1, 5, qq1)
            pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)

            pdf.set_text_color(redColor, greenColor, blueColor)
            pdf.multi_cell(effective_page_width / 1, 5, qqa)
            pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)
            pdf.set_text_color(0, 0, 0)

        pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)

        # Manual Q with A
    pdf.cell(ln=1, h=20.0, align='L', w=0, txt="", border=0)
    pdf.set_font('times', 'B', 16)
    topic_manual = "Answers for Manually added Questions".encode('latin-1', 'replace').decode('latin-1')
    pdf.cell(0, 10, topic_manual, ln=True, align='C')
    pdf.ln(3)

    pdf.set_font('times', '', 12)

    for item in constants.manual_q_with_a:
        pdf.set_font('times', 'B', 14)
        q = "Question:".encode('latin-1', 'replace').decode('latin-1')
        qa = item['question'].encode('latin-1', 'replace').decode('latin-1')

        pdf.multi_cell(effective_page_width / 1.5, 5, q)
        pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)
        pdf.multi_cell(effective_page_width / 1.5, 5, qa)
        pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)

        if item['lecturer_answer'] != "":
            pdf.set_font('times', 'B', 12)
            pdf.set_text_color(0, 0, 0)
            qtaTitle = ("     Lecturer Answer:").encode('latin-1', 'replace').decode('latin-1')

            pdf.multi_cell(effective_page_width / 1, 5, qtaTitle)
            pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)
            pdf.set_text_color(0, 0, 0)

            pdf.set_font('times', '', 12)
            pdf.set_text_color(153, 0, 76)
            qta = (item['lecturer_answer']).encode('latin-1', 'replace').decode('latin-1')

            pdf.multi_cell(effective_page_width / 1, 5, qta)
            pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)
            pdf.set_text_color(0, 0, 0)

        if len(item['google_answer']) > 0:
            pdf.set_font('times', 'B', 12)
            pdf.set_text_color(0, 0, 0)
            qqga = ("     Google Answers").encode('latin-1', 'replace').decode('latin-1')
            pdf.multi_cell(effective_page_width / 1, 5, qqga)
            pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)

        for ans in item['google_answer']:
            pdf.set_font('times', '', 12)

            qq1 = ("Answer:    " + ans['a']).encode('latin-1', 'replace').decode('latin-1')
            qqa = ("Reference: " + ans['cited']).encode('latin-1', 'replace').decode('latin-1')

            pdf.multi_cell(effective_page_width / 1, 5, qq1)
            pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)

            pdf.set_text_color(redColor, greenColor, blueColor)
            pdf.multi_cell(effective_page_width / 1, 5, qqa)
            pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)
            pdf.set_text_color(0, 0, 0)

        pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)

    outputPdf = os.path.abspath(os.curdir) + "/tempStorage/generatedFiles/" + filename + '.pdf'

    pdf.output(outputPdf)
    constants.finalSavedDocumentPath = outputPdf
    tkinter.messagebox.showinfo(title='Success', message='pdf saved successfully')

    return True

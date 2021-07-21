import tkinter as tk
from tkinter import Tk
from tkinter import ttk

from PIL import Image, ImageTk

from components import qaExtractor
from components import quality_analyzer
from components import videoEditor
from components import voiceEnhancerTab
from components.subComponents import fullPlayer, progressWindow


class Main(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("Video Editor")
        self.state("zoomed")

        self.splash()

    def splash(self):
        self.iconbitmap("./assets/icons/video_editor_icon.ico")

        top_canvas = tk.Canvas(self, background='light yellow', height='500')
        progress_windows = progressWindow.getProgressWindowView(top_canvas)
        progress_windows.pack(side=tk.TOP)
        player_base = fullPlayer.getFullPalyerView(top_canvas)

        top_canvas.pack(fill='both', side=tk.TOP)

        nb = ttk.Notebook(self)
        nb.pack(fill='both', expand=True)

        f1 = tk.Frame(nb)
        tk.Label(f1, text="in frame 1").pack()

        f2 = tk.Frame(nb)
        tk.Label(f2, text="in frame 2").pack()

        im1 = Image.open("assets//icons//videoEditor.png")
        ph1 = ImageTk.PhotoImage(im1)

        im2 = Image.open("assets//icons//qa.png")
        ph2 = ImageTk.PhotoImage(im2)

        imgVoiceEnhancer = Image.open("assets//icons//icons8-audio-wave.png")
        phVoiceEnhancer = ImageTk.PhotoImage(imgVoiceEnhancer)

        icon_quality_analyzer = ImageTk.PhotoImage(Image.open("assets//icons//icons8-analyze-50.png"))

        nb.add(videoEditor.getView(nb), text="Video Editor", image=ph1, compound=tk.TOP)
        nb.add(qaExtractor.getView(nb), text="Q&A Extractor", image=ph2, compound=tk.TOP)
        nb.add(voiceEnhancerTab.getView(nb), text="Voice enhancer", image=phVoiceEnhancer,
               compound=tk.TOP)
        nb.add(quality_analyzer.getView(nb), text="Quality Analyzer", image=icon_quality_analyzer, compound=tk.TOP)

        self.mainloop()

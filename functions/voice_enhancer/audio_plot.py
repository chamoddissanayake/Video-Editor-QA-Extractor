import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
import matplotlib
import librosa as lr
import numpy as np
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
    NavigationToolbar2Tk)

matplotlib.use("TkAgg")

def onselect_function(min_value, max_value):
    print(min_value)
    print(max_value)
    return min_value, max_value


def get_audio_amp_graph_data(audio_path):
    audio, sFreq = lr.load('D:/MyProjects/RESEARCH-PROJECT-FINAL-YEAR/2021-064/tempStorage/convertedAudio/1618463350.mp3')
    time = np.arange(0, len(audio)) / sFreq
    print(audio)
    print(time)

    return audio, time



# plot function is created for
# plotting the graph in
# tkinter window
def plot(frame):
    # the figure that will contain the plot
    # fig = Figure(figsize=(5, 5),
    #              dpi=100)

    fig, ax = plt.subplots()
    audio, time = get_audio_amp_graph_data("")
    ax.plot(time, audio)

    span = SpanSelector(
        ax,
        onselect=onselect_function,
        direction='horizontal',
        minspan=40,
        useblit=True,
        span_stays=True,
        button=1,
        rectprops={'facecolor': 'lightblue', 'alpha': 0.4}
    )

    # list of squares
    y = [i ** 2 for i in range(101)]

    # adding the subplot
    plot1 = fig.add_subplot(ax)

    # plotting the graph
    # plot1.plot(time, audio)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=frame)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().place(x=200, y=20)

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   frame)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
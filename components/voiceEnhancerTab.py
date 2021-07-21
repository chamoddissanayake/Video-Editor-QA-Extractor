import tkinter as tk
from functions.voice_enhancer import enhance_voice
from functions.voice_enhancer.audio_plot import plot

def getView(notebook):
    f1 = tk.Frame(notebook, bg="light blue")

    # frm1 = \
    # fullPlayer.getFullPalyerView(f1)d

    # frm1.pack(side=tk.LEFT)

    # frm3 = \
    # progressWindow.getProgressWindowView(f1)
    # frm3.pack(side=tk.BOTTOM)

    start_voice_enhancer_btn = tk.Button(f1, text='Start voice enhancer',
                                         command=lambda: enhance_voice.start_voice_enhancer())
    start_voice_enhancer_btn.place(x=20, y=60)

    f_plot = tk.Frame(f1, bg='light green')

    '''
        For noise_reducer
    '''
    # button that displays the plot
    # plot_button = tk.Button(master=notebook,
    #                         command=plot(f1),
    #                         height=2,
    #                         width=15,
    #                         text="Show audio graph")
    #
    # # place the button
    # # in main window
    # plot_button.place(x=30, y=200)

    # button_bonus = tk.Button(f1, text="Noise reduce", command=popup_window)
    # button_bonus.place(x=20, y=100)

    return f1


def popup_window():
    window = tk.Toplevel()

    label = tk.Label(window, text="Noise reducer will be implemented here")
    label.pack(padx=50, pady=5)

    button_close = tk.Button(window, text="Close", command=window.destroy)
    button_close.pack(fill='x')
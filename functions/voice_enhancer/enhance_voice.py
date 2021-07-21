from functions.voice_enhancer import audio_plot
from functions.voice_enhancer.topic_extractor.LDA_test import run_lda_topic_extraction
from utils.assembly_ai import speech_to_text
from utils import constants
import time as time
# import audio_plot
from utils import  constants
from components.subComponents import progressWindow
import random
from utils.converters.videoToAudioConverter import videoToAudioConverter
import tkinter.messagebox
import os

"""
    Lecturer Voice Enhancer
    @author : Nisuga Jayawardana (it18117110@my.sliit.lk)

    Objectives:
        1. Get the transcription of the video.
        2. Extract topic words from Topic Modelling - Gensim
        3. Set prosodic modifications to topic words using SSML (https://app.resemble.ai/docs#speech-synthesis-markup-language-ssml-reference)
        4. In the main transcription(SSML version), replace modified SSML elements with topic words
        5. Synthesise voice for the whole recording and generate an audio file from resemble.ai
        6. Replace the original audio of the video recording with the generated audio.

    Limitations:
        * The lecturer must have a cloned voice at resemble.ai
        * The generated synthesized voice may not match the explanations in the video
"""


def start_voice_enhancer():
    print("🎙🎙🎙 Starting Voice Enhancer 🎙🎙🎙")

    # Get extracted audio of the video recording
    audio_file = constants.converted_audio_path
    if len(audio_file) <= 0:
        print("No extracted audio found.")
        print("Extracting the audio from the video....")
        conversion_ok = videoToAudioConverter(constants.new_video_import_path, time.time())
        if not conversion_ok:
            message = "Failed to extract audio. Check whether a video is selected"
            print(message)
            tkinter.messagebox.showinfo(title='Error', message=message)
            return

    audio_file = constants.converted_audio_path
    print(audio_file)

    # Plot the audio - amplitude graph
    # audio_plot.get_audio_amp_graph()

    # Ask user to select a noisy part where no speaking happens.

    # Remove background noise using noisereduce py lib

    # Generate lecturer's transcription of the audio
    lecturer_transcription = speech_to_text.get_transcription_from_assembly_ai(audio_file)
    transcription_file_name = str(random.randint(100, 10000))+".txt"
    current_dir = os.path.abspath(os.curdir)
    f_path = current_dir + "/tempStorage/voiceEnhancerTranscriptions/" + transcription_file_name
    print(f_path)
    f = open(f_path, "w")
    f.write(lecturer_transcription)
    f.close()
    print(f'transcription saved {f_path}')

    # Initialize Topic word extractor
    # Preprocess the corpus of the transcription
    # Train the LDA Model using preprocessed_corpus
    # Get topic words with LDA output
    run_lda_topic_extraction(f_path)

    # Setup up prosodic parameters for each topic word, based on it's topic value

    # Generate SSML elements for each topic word by applying the prosodic parameters

    # Format the transcription to a basic SSML document.

    # Replace the  topic words in the SSMl document, with the generated SSML elements

    # Validate the final SSML Document.

    # send the final SSML Document resemble.ai API

    # Download the generated audio file

    # Ask user to preview the generated audio file.

    # If satisfied, Ask user to place the new audio file at a suitable starting point in the video timeline.
    # Else, cancel the process.

    # After user's confirmation, replace the audio with the new audio file.

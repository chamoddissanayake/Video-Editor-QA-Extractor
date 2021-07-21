import sys
import subprocess
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
import re

input_path = r"C:\Users\DELL\Videos\second_record.mkv"
out_path = r"C:\Users\DELL\Videos\editedsecond_recordVideo_test.mkv"
noise = 2
duration = 1

try:
    ease = float(sys.argv[5])
except IndexError:
    ease = 0.2

minimum_duration = 1.0

frozenCount = 0

def generate_timestamps(path, noise, duration):
    cmd = "ffmpeg -hide_banner -nostats -an  -i " + input_path + " -vf freezedetect=n=-60dB:d=3 -map 0:v:0  -f null - 2>&1 "
    #>ffmpeg -hide_banner -nostats -an -i C:\Users\DELL\Videos\record_test.mkv -vf "freezedetect=n=-60dB:d=2" -map 0:v:0 -f null -
    #command = "detect_frozen_frames {} {} {}".format(input_path, noise, duration)
    output = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    output = output.stdout.split("\n")[:-1]
    timestamps = []

    string = format(output)
    substring = "freeze_start:"

    frozenCount = string.count(substring)

    for line in output:
        if (line.find(': ') != -1):
            timestamps.append(line.split(": ")[1])

    timestamps.append(frozenCount)
    return timestamps


def main():
    count = 0
    last = 0
    timestamps = generate_timestamps(input_path, noise, duration)
    print("Timestamps: {}".format(timestamps))
    video = VideoFileClip(input_path)
    full_duration = video.duration
    clips = []

    arractCount = len(timestamps)
    frozenCount = timestamps[arractCount-1]

    arrayStart = arractCount - frozenCount*3 - 2
    arrayEnd = arractCount - 2

    newTimestamp = timestamps[arrayStart:arrayEnd]

    print(newTimestamp)



    for i in range(0, len(newTimestamp) - 1, 3):
        print("Index: ", i)
        start = float(last)
        end = float(newTimestamp[i + 2])
        to = float(newTimestamp[i]) + ease

        clip_duration = float(to) - start
        # Clips less than one seconds don't seem to work
        print("Clip Duration: {} seconds".format(clip_duration))

        if clip_duration < minimum_duration:
            continue

        if full_duration - to < minimum_duration:
            continue

        print("Clip {} (Start: {}, End: {})".format(count, start, to))
        clip = video.subclip(start, to)
        clips.append(clip)
        last = end
        count += 1

    if not clips:
        print("No frozen frames detected, exiting...")
        return

    if len(newTimestamp) % 2 == 0 and full_duration - float(last) > minimum_duration:
        print("Clip {} (Start: {}, End: {})".format(count, last, 'EOF'))
        clips.append(video.subclip(last))
    else:
        to = newTimestamp[-1]
        print("Clip {} (Start: {}, End: {})".format(count, last, to))
        clips.append(video.subclip(last, to))

    print(clips)

    processed_video = concatenate_videoclips(clips)
    processed_video.write_videofile(
        out_path,
        fps=60,
        preset='ultrafast',
        codec='libx264',
        audio_codec='aac'
    )

    video.close()


main()

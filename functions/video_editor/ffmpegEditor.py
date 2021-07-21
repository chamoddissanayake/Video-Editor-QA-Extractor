import subprocess
# import ffmpeg
import sys
import os
from moviepy.editor import concatenate_videoclips, VideoFileClip
import re

input_path = r"C:\Users\DELL\Videos\reaserch_video.mkv"
out_path = r"C:\Users\DELL\Videos\editedreaserch_video.mkv"
#threshold = 2
#duration = 1

# Ease in duration between cuts
# from functions.video_editor.editSilentVideo import generate_timestamps

try:
    ease = float(sys.argv[5])
except IndexError:
    ease = 0.2

minimum_duration = 1.0


# file_name, ext = os.path.splitext(file_in)


# class FFMConvertor:

def generate_timestamps(threshold, duration):
    cmd = "ffmpeg -hide_banner -vn -i " + input_path + " -af silencedetect=n=-" + threshold + "dB:d=" + duration + ",ametadata=print:file=log.txt -f null - 2>&1 "

    output = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    # f = open("videoTimeStamp.txt", "w+")
    # f.write(output)

    # output = subprocess.run(command, shell=True, capture_output=True, text=True)
    return output.stdout.split('silence_start:')[:-1]


def mainAudio(threshold, duration):
    count = 0
    last = 0
    timestamps = generate_timestamps(threshold, duration)

    print("Timestamps: {}".format(timestamps))

    video = VideoFileClip(input_path)
    full_duration = video.duration
    clips = []

    count = 1
    cnt = 0

    for times in timestamps:
        if count == 1:
            count = 2
        else:
            p = re.compile(r'\d+\.\d+')  # Compile a pattern to capture float values
            tt = format(times)
            floats = [float(i) for i in p.findall(tt)]  # Convert strings to float
            print(floats)

            listToStr = ' '.join(map(str, floats))
            print(listToStr)
            count = 3

            arractCount = len(floats)

            if arractCount == 2:
                end, dur = listToStr.strip().split()
            elif arractCount == 3:
                sta, end, dur = listToStr.strip().split()

            print("End: {}, Duration: {}".format(end, dur))

            to = float(end) - float(dur) + ease

            start = float(last)
            clip_duration = float(to) - start
            # Clips less than one seconds don't seem to work
            print("Clip Duration: {} seconds".format(clip_duration))

            if clip_duration < minimum_duration:
                continue

            if full_duration - to < minimum_duration:
                continue

            print("Clip {} (Start: {}, End: {})".format(cnt, start, to))
            clip = video.subclip(start, to)
            clips.append(clip)
            last = end
            cnt += 1

    if not clips:
        print("No silence detected, exiting...")
        return

    if full_duration - float(last) > minimum_duration:
        print("Clip {} (Start: {}, End: {})".format(count, last, 'EOF'))
        clips.append(video.subclip(last))

    processed_video = concatenate_videoclips(clips)
    processed_video.write_videofile(
        out_path,
        fps=60,
        preset='ultrafast',
        codec='libx264',
        audio_codec='aac'
    )

    video.close()


#main()


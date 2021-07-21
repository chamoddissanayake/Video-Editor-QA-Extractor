from proglog import ProgressBarLogger

from components.subComponents import progressWindow
from utils import value


class MyBarLogger(ProgressBarLogger):
    full_count = 0
    current_count = 0
    def callback(self, **changes):

        for (parameter, new_value) in changes.items():
            print ('Parameter %s is now %s' % (parameter, new_value))

    def bars_callback(self,bars, attr, value, old_value):
        if attr == 'total':
            self.full_count = value
        else:
            self.current_count = value
            self.calculateCurrentPresentage()

    def calculateCurrentPresentage(self):
        progress = (self.current_count/self.full_count)*100
        progressWindow.status_label.config(text="Converting video to audio")
        if progress == 100:
            progressWindow.status_label.config(text="Converted video to audio")
        value.video_to_audio_convert_progress = progress
        progressWindow.bar(value.video_to_audio_convert_progress)
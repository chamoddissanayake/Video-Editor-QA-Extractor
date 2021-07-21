import datetime

"""
Author: Bandara A.B.C.N
Student ID: IT18117356
Group ID: 2021-064
"""


class PeriodCheck:
    def __init__(self, frames, period):
        """
        Args:
            frames: Analyzed frames
            period: no need minimum time period
        """
        self.__frames = frames
        self.__period = period

    def __empty_parts(self):
        """
        Returns: A 2D list, the length of a sub-list is 2
        """
        segment = []
        segments = []

        # loop through frames of current object
        for index, value in enumerate(self.__frames):
            if index + 1 == len(self.__frames):
                # append the current value to segment
                segment.append(value)
                # append the current segment into segments list
                segments.append(segment)
                break

            # check if the current value + 1 is equal to next index value then
            if self.__frames[index + 1] == value + 1:
                # if segment is empty then
                if len(segment) == 0:
                    # append the current value into segment list
                    segment.append(value)
            else:
                # append the current value to segment
                segment.append(value)
                # append the current segment into segments list
                segments.append(segment)
                # empty current segment
                segment = []
        # if the segment length is not equal two then remove from the list
        return [segment for segment in segments if len(segment) == 2]

    def __no_need_parts(self):
        """
        Returns: A 2D list, the length of a sub-list is 2
        """
        parts = []

        # loop through segments of __empty_parts
        for segment in self.__empty_parts():
            # if the first value - second value of the segment is equal to period - 1 then
            if segment[1] - segment[0] >= self.__period - 1:
                # append the segment to parts list
                parts.append(segment)

        # return the parts list
        return parts

    def periods(self, fps):
        """
        Args:
            fps: frame per second of the current video
        Returns: A 2D list, the length of a sub-list is 2
        """
        segment = []
        segments = []

        # loop through segments of __no_need_parts
        for period in self.__no_need_parts():
            # convert each count value into time and append to segments
            for i in period:
                result = str(datetime.timedelta(seconds=i / fps))
                # remove the floating point digit in a second
                no_float = result.split(".")[0]
                segment.append(no_float)

            segments.append(segment)
            segment = []

        # return segments
        return segments

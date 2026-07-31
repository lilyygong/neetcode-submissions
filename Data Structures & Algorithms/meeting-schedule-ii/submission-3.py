"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = []
        end_times = []
        i = 0
        j = 0
        total_rooms = 0
        curr_rooms = 0
        for a in range(len(intervals)):
            start_times.append(intervals[a].start)
            end_times.append(intervals[a].end)
        start_times.sort()
        end_times.sort()

        while i < len(start_times):
            if start_times[i] < end_times[j]:
                print(start_times[i], end_times[j])
                curr_rooms += 1
                total_rooms = max(total_rooms, curr_rooms)
                i += 1
            else:
                j += 1
                curr_rooms -= 1
        return total_rooms
        # for i in range(len(start_times)):
        #     for j in range(len(end_times)):
        #         if start_times[i] < end_times[j]:
        #             curr_rooms += 1
        #             total_rooms += 1
        #             break
        #         else:
        #             curr_rooms -= 1
        #             break
        
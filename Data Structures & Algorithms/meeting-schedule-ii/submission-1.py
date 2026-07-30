"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)
        start.sort()
        end.sort()
        max_rooms = 0
        rooms = 0
        s = 0
        e = 0
        while s < len(intervals):
            if start[s] < end[e]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                s += 1
            else:
                rooms -= 1
                e += 1
        return max_rooms


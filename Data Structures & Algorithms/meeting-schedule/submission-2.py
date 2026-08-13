"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # overlapping 이면 False 아니면 True
        if len(intervals) == 0:
            return True
        intervals.sort(key = lambda x:x.start)
        prevEnd = intervals[0].end
        for i in range(1, len(intervals)):
            if prevEnd > intervals[i].start:
                return False
            prevEnd = intervals[i].end
        return True
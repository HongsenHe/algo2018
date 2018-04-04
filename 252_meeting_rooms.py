# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        '''
        按照开始时间排序，看每个房间的结束时间，如果大于下一个房间的开始时间，拖堂了！
        '''
        
        # sort by first start
        intervals.sort(key=lambda x: x.start)
        for i in range(0, len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True
        
        
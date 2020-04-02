class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        
        # 按照开始时间排序，看每个房间的结束时间，如果大于下一个房间的开始时间，拖堂了！

        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True

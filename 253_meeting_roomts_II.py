# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        
        '''
        先按照开始时间排序, 用一个数列指保存每个房间的结束时间，数列大小即房间多少。
        对于每一个房间，如果开始时间小于数列中最早结束时间，即要开一个新的房间
        因为人家都还没结束，你就开始了，另起炉灶。这里需要最小堆找到最早结束时间。
        如果大于等于，证明这个房间还可以加会议，更新结束时间。
        '''
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x :x.start)
        heap = [] # min heap, save each room release time
        for interval in intervals:
            if heap and interval.start >= heap[0]:
                # update this room release time
                heapq.heapreplace(heap, interval.end)
            else:
                # add a new room and set release time
                heapq.heappush(heap, interval.end)
                
        return len(heap)
        
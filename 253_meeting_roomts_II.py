import heapq

class Solution:
    '''
    先按照开始时间排序, 用一个数列指保存每个房间的结束时间，数列大小即房间多少。
    对于每一个房间，如果开始时间小于数列中最早结束时间，即要开一个新的房间
    因为人家都还没结束，你就开始了，另起炉灶。这里需要最小堆找到最早结束时间。
    如果大于等于，证明这个房间还可以加会议，更新结束时间。
    '''
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x :x[0])
        # 为什么要和最早结束时间比？因为这样可以判断当前会议是否能接上最早结束的会议并且继续使用教室
        # 如果这都无法满足，另起炉灶比较好。
        heap = [] # min heap, save each room release time
        for interval in intervals:
            # 如果当前的会议开始时间3pm大于最早结束时间2pm, 可以继续用这个教室但要更新结束时间
            if heap and interval[0] >= heap[0]:
                # update this room release time
                heapq.heapreplace(heap, interval[1])
                
                # or use
                # heapq.heappop(heap)
                # heapq.heappush(heap, interval[1])
            else:
                # 如果当前的会议开始时间1pm 小于最早结束时间2pm, 则另起炉灶放到heap里
                # add a new room and set release time
                heapq.heappush(heap, interval[1])
                
        return len(heap)
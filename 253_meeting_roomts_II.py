import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 10262021 不用heap...
        room_count = 0
        rooms_end = []
        
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        for interval in sorted_intervals:
            new_room = True
            
            start = interval[0]
            end = interval[1]
            
            for i in range(len(rooms_end)):
                if start >= rooms_end[i]:
                    rooms_end[i] = end
                    new_room = False
                    break
                    
            if new_room:
                room_count += 1
                rooms_end.append(end)
                
        return room_count



        # 05132021
            '''
        heap 经典应用
        先按照开始时间排序，确保一个参数(start)是升序的。
        用min heap来存下课时间。如果当前的开始时间比下课时间早，
        那就要再开一个房间，并且把当前课程的下课时间存进去。
        
        如果开始时间比下课晚，继续等 即可以使用此教室，因为按照开始时间排序了。
        所以不存在插队现象。
        同时把正在进行的课程(peak) 弹出来，放入当前课程的结束时间。
        
        '''
        intervals.sort(key=lambda x: x[0])
        heap = []
        heapq.heappush(heap, intervals[0][1])
        room = 1
        
        for start, end in intervals[1:]:
            # 前一个还没下课就开始了，重新开一个房间， 并且更新保留最小ending time作为peak
            if start < heap[0]:
                room += 1
                heapq.heappush(heap, end)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, end)
                    
        return room
            

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
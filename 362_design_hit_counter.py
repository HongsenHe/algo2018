from collections import deque

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # deque快很多。
        self.queue = deque()
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.queue.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        
        '''
        03092022
        和findFirstUnique题一样，查找当前头部数字是否合格。
        FFU是，如果queue[0]不是unique的，则queue.popleft()
        此题是，如果queue[0] 小于等于cur timestamp - 300
        即301 - 300 = 1， 则queue.popleft() 把1删掉。
        重复操作，知道当前queue都符合标准。
        '''
        while self.queue and timestamp - self.queue[0] >= 300:
            self.queue.popleft()
            
        return len(self.queue)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


class HitCounter:

    '''
    此方法会遍历所有dic, 其实没必要

    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp in self.dic:
            self.dic[timestamp] += 1
        else:
            self.dic[timestamp] = 1
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        res = 0
        for ts, cnt in self.dic.items():
            if ts > timestamp - 300:
                res += cnt
        return res

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
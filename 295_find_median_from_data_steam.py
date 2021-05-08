import heapq

class MedianFinder:

    def __init__(self):
        self.first_heap = [] # this is max heap, save the first half of nums
        self.second_heap = [] # min heap, save the 2nd half of nums
        

    def addNum(self, num: int) -> None:
        '''
        先把这个数插入前半段(first_heap), 等调整过后peak就是最大值
        再把peak扔进后半段(second_heap), 调整过后就算有了顺序（median的两个点）
        再调整两个heap的大小，保证前半段总是>= 后半段就行。
        如果满足，把后半段吐出来，前半段吃进去。
        '''
        heapq.heappush(self.first_heap, -num)
        heapq.heappush(self.second_heap, -heapq.heappop(self.first_heap))
        
        if len(self.first_heap) < len(self.second_heap):
            heapq.heappush(self.first_heap, -heapq.heappop(self.second_heap))
            
        

    def findMedian(self) -> float:
        # 如果前半段已经大于后半段了，说明整个nums是奇数，返回前半段的顶就好
        if len(self.first_heap) > len(self.second_heap):
            return -self.first_heap[0]
        
        # 前后半段两个顶已经求解
        return (float(-self.first_heap[0]) + float(self.second_heap[0])) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        heapq.heapify(listForTree)             # for a min heap
        heapq._heapify_max(listForTree)        # for a maxheap!!
        heapq.heappop(minheap)      # pop from minheap
        heapq._heappop_max(maxheap) # pop from maxheap

        '''
        heap = [-stone for stone in stones]
        heapq.heapify(heap) # O(n)
        
        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, y-x)

        return -heapq.heappop(heap) if heap else 0
        
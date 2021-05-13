import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        heapq.heappush(heap, 1)
        
        visited = set()
        visited.add(1)
        
        res = 0
        
        for i in range(n):
            res = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                if res * factor not in visited:
                    visited.add(res * factor)
                    heapq.heappush(heap, res * factor)
                    
        return res
        
        
        
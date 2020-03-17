import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for point in points:
            dis = self.get_distance(point)
            heapq.heappush(heap, (dis, point)) 
        res = []
        while K > 0:
            res.append(heapq.heappop(heap)[1])
            K -= 1
                
        return res
    
    def get_distance(self, point):
        return pow(abs(point[0]), 2) + pow(abs(point[1]), 2)
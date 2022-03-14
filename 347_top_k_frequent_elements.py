import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        03132022
        python heap 默认是min heap. 如果维持一个size = k的heap, 
        则每次都要弹出去，只保留K最多的数字，即把cnt最小的pop掉，用min heap
        
        如果不做if pop 操作，即一直添加，heap size = len(nums)
        最后进行pop K个的时候，则需要把cnt最大的num 弹出来，此时用max heap
        则在build的时候，需要用-cnt来push 到 heap中去。
        
        '''
        heap = []
        
        num_cnt = Counter(nums)
        
        for num, cnt in num_cnt.items():
            heapq.heappush(heap, (cnt, num))
            
            if len(heap) > k:
                heapq.heappop(heap)
                
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
            
        return res
    
#         heap = []
#         nums_dict = Counter(nums)
        
#         for num, cnt in nums_dict.items():
#             heapq.heappush(heap, (-cnt, num))
            
#         res = []
#         for i in range(k):
#             res.append(heapq.heappop(heap)[1])
            
#         return res
        
        




from Queue import PriorityQueue 

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        '''
        # solution 1, just sort dictionary by value, time O(nlgn), 61ms
        tf = {}
        for num in nums:
            if num in tf:
                tf[num] += 1
            else:
                tf[num] = 1
        
        # time O(nlgn)
        tf2 = sorted(tf.items(), key=lambda x:x[1], reverse=True)
        
        res = []
        for i in range(k):
            res.append(tf2[i][0])
        return res
        '''
            
        
        # solution 2, one line thing, 69ms
        # return [i[0] for i in collections.Counter(nums).most_common(k)]
        
        
        # solution 3, heapq in Python, 97ms
        import heapq

        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            heap = []
            nums_dict = Counter(nums)
            
            for num, cnt in nums_dict.items():
                heapq.heappush(heap, (-cnt, num))
                
            res = []
            for i in range(k):
                res.append(heapq.heappop(heap)[1])
                
            return res
        
        
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
        
        
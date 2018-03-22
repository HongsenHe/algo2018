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
        
        
        # solution 3, priority queue (max heap), 97ms

        # a shorter way to build a term freq dic
        tf = collections.Counter(nums) 
        q = PriorityQueue() # a min-heap by default, so need reverse
        for kk, v in tf.items():
            q.put((-v, kk)) # to be a max heap
        
        res = []
        for i in range(k):
            res.append(q.get()[1])
        return res
        
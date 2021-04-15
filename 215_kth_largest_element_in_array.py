import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            heapq.heappush(q, num)
            
            # keep push to min heap, but only keep k size
            # otherwise pop the number, time O(nlogk)
            if len(q) > k:
                heapq.heappop(q)
                
        return heapq.heappop(q)
                
        
        # O(nlogn) 04152021
        nums.sort()
        return nums[len(nums) - k]
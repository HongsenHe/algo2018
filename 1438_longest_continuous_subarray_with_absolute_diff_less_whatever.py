class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_d = deque()
        min_d = deque()
        i = 0
        res = 0
        
        # 维护两个queue分别包含当前window内最大、最小值。
        # 根据当前条件不断调整i， 获得最长子序列
        
        for j,n in enumerate(nums):
            while max_d and n > max_d[-1]:
                max_d.pop()
            max_d.append(n)

            while min_d and n < min_d[-1]:
                min_d.pop()
            min_d.append(n)

            while max_d[0] - min_d[0] > limit:
                if max_d[0] == nums[i]:
                    max_d.popleft()
                if min_d[0] == nums[i]:
                    min_d.popleft()
                i += 1
            res = max(res,(j-i+1))            

        return res
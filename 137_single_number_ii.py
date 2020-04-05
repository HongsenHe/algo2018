from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mp = Counter(nums)
        for k, v in mp.items():
            if v == 1:
                return k

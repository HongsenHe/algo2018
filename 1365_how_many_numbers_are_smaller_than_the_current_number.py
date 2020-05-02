class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            cnt = 0
            for num2 in nums:
                if num2 < num:
                    cnt += 1
            res.append(cnt)
            
        return res
                
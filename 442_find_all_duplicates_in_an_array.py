class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        for num in nums:
            # current number, 4 but idx should be 3
            idx = abs(num) - 1
            # if first time, assign -3 to nums[3]
            # if sec, current element < 0, put that into res
            if nums[idx] < 0:
                res.append(abs(num))
            else:
                nums[idx] = -nums[idx]
        return res
                
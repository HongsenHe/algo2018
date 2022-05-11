class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        res = []
        for num in nums:
            res.append(a * num * num + b * num + c)
            
        return sorted(res)
            
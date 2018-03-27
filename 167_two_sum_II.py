class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            subSum = numbers[left] + numbers[right]
            if subSum == target:
                return [left+1, right+1]
            elif subSum < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]
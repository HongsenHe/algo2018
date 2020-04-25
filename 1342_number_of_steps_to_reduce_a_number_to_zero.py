class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0
        while num != 0:
            if num % 2 == 1:
                num -= 1
            else:
                num = num // 2
            steps += 1
        return steps

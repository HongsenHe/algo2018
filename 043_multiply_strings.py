class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        123 x 4 = 4x3 + 4x20 + 4x100, k1就是每循环一次num1 扩大十倍，并且乘以基数 
        与num2 当前的数字相乘 即: num * int(num[l]) * k1
        同样，每循环一次num2的数字，k2也扩大十倍
        """
        if num1 == "0" or num2 == "0":
            return "0"
        # by default num2 is shorter than num1
        if len(num1) < len(num2):
            res = self.helper(num2, num1)
        else:
            res = self.helper(num1, num2)
        return str(res)

    def helper(self, num1, num2):
        res, k2 = 0, 1
        for s in range(len(num2) - 1, -1, -1):
            num = int(num2[s]) * k2
            k1 = 1
            for l in range(len(num1) - 1, -1, -1):
                res += num * int(num1[l]) * k1
                k1 *= 10
            k2 *= 10
        return str(res)

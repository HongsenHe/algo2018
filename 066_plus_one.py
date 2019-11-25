class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        res = []
        for i in range(len(digits)-1, -1, -1):
            cur = digits[i] + carry
            if cur >= 10:
                cur = cur - 10
                carry = 1
                res.insert(0, cur)
            else:
                res.insert(0, cur)
                # if current result is < 10, just copy the rest of nums
                for j in range(i-1, -1, -1):
                    res.insert(0, digits[j])
                return res
        if carry == 1:
            res.insert(0, 1)
        return res
            
            
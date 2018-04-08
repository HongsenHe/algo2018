class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        i = 0
        res = []
        
        while num > 0:
            rom = num // nums[i]
            num = num % nums[i]
            
            for j in range(rom):
                res.append(roman[i])
            i += 1
        return ''.join(res)
                
      
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        res = []
        if not digits:
            return res
        self.helper(digits, '', res, phone)
        return res
    
    def helper(self, digits, each_res, res, phone):
        # 经典回溯套路：边际条件，大循环取当前，把下一个扔进去继续跑
        '''
        input: 23, 2-> a, b, c; 3-> d, e, f
        2开始，第一层循环是a, b, c
        第二层要循环3 对应的 d, e, f,分别和第一层的a 配合
        如果有第三层，就是a 配合第二层第一个d，然后走下去取g配合ad
        直到当前的digit没有了，也就是吧adg放进结果，
        再返回第三层也就是h, 配合ad, 即adg, 直到i
        返回第二层，a和d都配完，所以a和e搭配，直到f
        返回第一层，a和所有第二层配完，现在第一层是b, 依次和第二层配合
        
        时间复杂度和空间复杂度一样：
        数字2, 3, 4, 5, 6, 8 有三个字母，所以是3^n
        数字7, 9 有四个字母，是4^m, 
        复杂度: 3^n + 4^m, (n+m) 是所有输入数字的个数。
        '''
        if len(digits) == 0:
            res.append(each_res)
        else:
            for letter in phone[digits[0]]:
                self.helper(digits[1:], each_res+letter, res, phone)
            
        
        
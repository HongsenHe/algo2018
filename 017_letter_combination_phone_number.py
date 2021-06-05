
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
        
        # 全新做法 06052021!
        if not digits:
            return []
        
        res = []
        self.helper(res, digits, phone, [], 0)
        
        return res
    
    def helper(self, res, digits, phone, each, start):
        # 当前子集each个数符合条件，放入结果集里
        if len(each) == len(digits):
            each_str = ''.join(each)
            res.append(each_str)
            return
        
        '''
        两个数字23，需要用2的abc和3的def配对，则需要一个start pointer
        不停向前走，即在outer for loop使用start
        对于每一个数字2的字母集(abc), 需要和下一个字母集(def)配对，经典回溯法
        ad, ae, af, a这层都结束之后，则以b开头，即bd, be, bf， 以此类推
        '''
        
        for i in range(start, len(digits)):
            letters = phone[digits[i]]
            
            for letter in letters:
                each.append(letter)
                self.helper(res, digits, phone, each, i + 1)
                each.pop()
        
        
            


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
            
        
        
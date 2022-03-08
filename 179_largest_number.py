class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        '''
        先排序，但不是普通的排序。因为9不是最大也不是最小，但要排在前面。
        对比两个数字，a=3, b=30, 他们组合可能是ab=330 or ba=303
        ab > ba 所以3在30前面。
        
        '''
        res = ''.join(sorted(map(str, nums), key=LargerNum))
        return '0' if res[0] == '0' else res
        
class LargerNum(str):
    def __lt__(a, b):
        return a + b > b + a
    
    
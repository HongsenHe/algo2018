class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        '''
        此题和1062比较像，是隐式二分法。
        并不是二分这个list, 而是二分要切的范围。
        对于ribbons里最长的，把它的一般，即n/2
        看用这个size 所有ribbons能切多少份，如果超过K了
        则有优化空间(提高size) 也就是二分法，把left side省略
        即left = mid, 最后while loop出来，先看right idx
        是否满足答案。
        
        切一刀问题，相当于二分了。left = 1， 1是最小单位
        right 要初始于最长的那个。
        '''
        
        left = 1
        right = max(ribbons)
        
        # 最小单位是1，如果所有ribbons加一起（单位是1）< k, 则无解
        if k > sum(ribbons):
            return 0
        
        while left + 1 < right:
            mid = (left + right) // 2
            if self.get_cnt(ribbons, mid) >= k:
                left = mid
            else:
                right = mid
                
        if self.get_cnt(ribbons, right) >= k:
            return right
        
        return left
    
    def get_cnt(self, ribbons, size):
        res = 0
        for rib in ribbons:
            res += rib // size
            
        return res
    
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        '''
        substring的长度可能是1 to n-1, 如何缩小这个长度？即用二分法
        比如s 长度是16，那n/2 = 8, 看左substring是否等于右substring
        如果不等，则把substring length / 2，即长度是4，
        从头到尾，看长度是4的substring 是否能找到。
        如果找不到继续 n/2 = 2, 如果找到了（用set()) 则用3。
        最后答案是left的idx - 1
        
        套用经典二分法模板后，left/right 差一位相遇。
        要得到最大substring, 则先看right idx是否满足（是否有重复substring)
        如果满足则返回right idx.
        
        '''
        n = len(s)
        left = 0
        right = n - 1
        
        while left + 1 < right:
            size = (left + right) // 2
            
            if self.search(size, s) != -1:
                left = size 
            else:
                right = size
                
        # left/right指针相遇后，要找最大substring,所以先看right指针是否满足。
        if self.search(right, s) != -1:
            return right

        return left
        
    def search(self, size, s):
        visited = set()
        n = len(s)
        
        for start in range(n - size + 1):
            tmp = s[start: start + size]
            if tmp in visited:
                return start
            visited.add(tmp)
            
        return -1
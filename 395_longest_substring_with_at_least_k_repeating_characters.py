class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        counter = Counter(s)
        left = 0
        n = len(s)
        res = 0
        '''
        如果当前元素的个数< k, 则最后答案肯定不包含这个元素，即答案在当前元素的左右边。
        
        '''
        for i in range(n):
            # 当前元素个数不符合条件，搜左边，并且左窗口+1。当前元素为右窗口，并且每次递增
            if counter[s[i]] < k:
                res = max(res, self.longestSubstring(s[left: i], k))
                left += 1
        
        # 跳出递归，如果左窗口没有变过，则说明每个元素都符合条件，即s自己的长度就是答案
        if left == 0:
            return n
                
        # 对于当前的substring, (递归的核心，即相信这个function的功能。）
        # 左半部分最后再和右半部分比较，即使答案。
        res = max(res, self.longestSubstring(s[left: n], k))
        
        return res
        
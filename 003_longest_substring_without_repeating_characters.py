class Solution(object):
    # best, updated 04062020
    def lengthOfLongestSubstring(self, s):
        left = 0
        right = 0
        pool = set()
        res = 0
        
        while right < len(s):
            if s[right] not in pool:
                pool.add(s[right])
                right += 1
                res = max(res, len(pool))
            else:
                # if dup, remove 1 left element, even that one
                # is not the dup one.
                pool.remove(s[left])
                left += 1
        return res
                
    # better
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        dic = {}
        start = 0
        res = 0
        
        for end in range(len(s)):
            # 当在dic里找到一个重复值，并且这个值上一次的位置 >= 左边界(start)
            # 就更新左边界到这个数值的下一个位置，滑动窗口！
            if s[end] in dic and dic[s[end]] >= start:
                start = dic[s[end]] + 1
            # 并且在dic里更新这个数字的位置，用现在的index
            dic[s[end]] = end
            # 比较长度
            res = max(res, end-start+1)
        return res
            

    # naive!
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            count = 0
            visited = set()
            for j in range(i, len(s)):
                if s[j] in visited:
                    break
                count += 1
                visited.add(s[j])
                
            res = max(res, count)
        return res
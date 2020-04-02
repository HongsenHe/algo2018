class Solution(object):
    # best
    def lengthOfLongestSubstring(self, s):
        # keep maintain a distinct set, if dup found, remove from set
        pool = set()
        i = 0
        j = 0
        res = 0
        
        while j < len(s):
            # new char
            if s[j] not in pool:
                pool.add(s[j])
                j += 1
                res = max(res, len(pool))
            else:
                pool.remove(s[i])
                i += 1
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
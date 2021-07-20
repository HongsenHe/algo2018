class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        '''
        用一个dp[i] 存储状态，如果以第i个字母结尾，能不能行！
        设立一个index 把要求的subString 分割成两段，看分别行不行
        之前的一段可以用dp的值，因为是之前的，一定知道结果
        后面一段就看在不在字典里。
        好比leetcode, ['leet', 'cod', 'e']
        分析leetcod的时候，逐渐拆分，直到leet 是以前的结果dp[3]和cod在字典里
        所以leetcod就是True. 分析完leetcod之后，再继续加下一个字母e。你懂的。。。
        '''
        
        if not s or not wordDict:
            return False
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

        
        # for i in range(1, len(s)+1):
        #     first = s[0:i]
        #     if first in wordDict:
        #         second = s[i:]
        #         if not second or second in wordDict or self.wordBreak(second, wordDict):
        #             return True
        # return False
        
        
        @lru_cache
        def wordBreakMemo(s: str, word_dict: FrozenSet[str], start: int):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_dict and wordBreakMemo(s, word_dict, end):
                    return True
            return False

        return wordBreakMemo(s, frozenset(wordDict), 0)
    
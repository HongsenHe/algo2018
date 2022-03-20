class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        res = 0
        j = 0
        max_freq = 0
        
        '''
        创造滑动窗口，[i:j], 这里面出现最多的字符数量少 max_freq
        则， j - i - max_freq表示需要被替换的字母数量是多少。
        标准写法，一个for loop/while, 里面有另一个while loop来让fast pointer
        继续走 ，走到不满足条件跳出。即 j - i - max_freq <= k
        跳出后，看目前的答案和全局res打擂台。
        本次循环最后 要缩小左窗口，i++, 并且其数量减一。
        
        '''
        
        for i in range(len(s)):
            while j < len(s) and j - i - max_freq <= k:
                counter[s[j]] = counter.get(s[j], 0) + 1
                max_freq = max(max_freq, counter[s[j]])
                j += 1
                
            if j - i - max_freq > k:
                res = max(res, j - 1 - i)
            else:
                res = max(res, j - i)
                
            counter[s[i]] -= 1
            
        return res
        
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        m = len(s)
        n = len(p)
        
        if m < n:
            return res
        
        '''
        goal: comparing p_cnt == s_cnt, p_cnt is the target
        key is letter ascii number, value is the count
        s_cnt is the same thing of the sliding window
        
        how to maitain the sliding window?
        s_cnt 就是当前窗口里的字母和其数量的字典！如果长度超过了p，每次缩小left
        
        two pointers, in every loop round:
        add right letter and update s_cnt and increment the value +1
        if current index i >= len(p), it's time to think about removing
        left pointer from s_cnt
        then after these operations, compare p_cnt and s_cnt
        '''
        p_cnt, s_cnt = [0] * 26, [0] * 26
        
        # init p_cnt, key is letter value is count
        for c in p:
            p_cnt[ord(c) - ord('a')] += 1
            
        for i in range(m):
            # add a letter on the right 
            s_cnt[ord(s[i]) - ord('a')] += 1
            
            # if current index i >= len(p), then remove left one, sliding window
            if i >= n:
                s_cnt[ord(s[i-n]) - ord('a')] -= 1
                
            # check sliding window and target p_cnt
            if s_cnt == p_cnt:
                res.append(i - n + 1)
        return res
                
            
                
        
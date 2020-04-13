class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        
        '''
        最终比较s1_cnt == s2_cnt
        s1_cnt就是小的s1的字母与个数的字典
        s2_cnt就是滑动窗口，不断创建，如果相等就是字母和个数相等，返回True
        滑动窗口：每次循环都要把当前的i 也就是右指针的字母和个数update s2_cnt
        如果当前i>= 目标s1的长度，就要开始减去左指针left，即i-len(s1)
        每次都减去左指针的字母个数
        
        当更新完 还相等，就是答案了。
        '''
        s1_cnt, s2_cnt = [0] * 26, [0] * 26
        for s in s1:
            s1_cnt[ord(s) - ord('a')] += 1
            
        for i in range(len(s2)):
            s2_cnt[ord(s2[i]) - ord('a')] += 1
            
            if i >= len(s1):
                s2_cnt[ord(s2[i - len(s1)]) - ord('a')] -= 1
                
            if s2_cnt == s1_cnt:
                return True
            
        return False
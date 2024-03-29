class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 04092021
        '''
        看到permutation并不是要求所有排列的组合，其本质是s1里有多少个a多少个b...
        也就是求每个字母的数量。
        对于一个str包含另一个str的问题，可以考虑滑动窗口问题。
        这里面从头开始，选固定长度，依次比较字母的数量。
        然后继续滑动，头减1，尾加1的模式，直到找到答案。
        '''
        
        l1 = len(s1)
        target = collections.Counter(s1)
        
        for i in range(len(s2) - l1 + 1):
            # 如果当前字母都不在s1里，可以忽略
            if s2[i] in target:
                # 这里的sub_s2就是以i为起点，固定长度是s1的 substring
                # 然后再看这个string的 字母数量，如果和s1相等就 True!
                sub_s2 = collections.Counter(s2[i : i + l1])
                if sub_s2 == target:
                    return True
                
        return False




        if not s1 or not s2:
            return False
        
        '''
        最终比较s1_cnt == s2_cnt
        s1_cnt就是小的s1的字母与个数的字典
        s2_cnt就是滑动窗口，不断创建，如果相等就是字母和个数相等，返回True
        滑动窗口：每次循环都要把当前的i 也就是右指针的字母和个数update s2_cnt
        如果当前i>= 目标s1的长度，就要开始减去左指针left，即i-len(s1)
        每次都减去左指针的字母个数, 当更新完还相等，就是答案了。
        
        套路就是构建一个26长度的list，存每个字母出现的个数，也可以每次都sort然后比较
        如果个数相等那肯定就相等了。每次移动窗口就不断加减字幕的个数。
        
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
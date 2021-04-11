from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_count = Counter()
        t_count = Counter(t)
        res = []
        left, right = 0, 0
        
        '''
        同向双指针维持滑动窗口问题，以右指针为主，一直走直到满足条件。
        s_count & t_count 代表他们的交集，也就是即使s_count里
        有很多其他字母但只要有和t_count 字母数量一样就行。
        
        右指针停止后，开始滑动左指针，要尽量缩小范围以求最优解。
        左指针不停的移动，同时减少相应的在s_count里的字母。
        知道破坏了已有条件，即 s_count & t_count 交集字母的数量
        不等于target(t_count)了。此时把结果加入res中。
        既然已经破坏了窗口，起始点就是当前left的前一个，即 left - 1
        right已经 越界，所以到right就好。
        
        最后比较，注意Python语法 min(res, key=len)
        以len排序，找最小的一个答案。
        
        '''
        
        
        while right < len(s):
            s_count[s[right]] += 1
            right += 1
            
            if s_count & t_count != t_count:
                continue

            while left < right:
                s_count[s[left]] -= 1
                left += 1
                if s_count & t_count == t_count:
                    continue
            
                res.append(s[left - 1: right])
                break
                
        if not res:
            return ""
        
        return min(res, key=len)
                
            
        
        
        
        
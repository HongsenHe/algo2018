class Solution(object):
    # 套用模板，updated 04102021
    '''
    同向双指针解决substring问题。设快慢指针来创造滑动窗口。
    快指针(right) 一直跑 right += 1，
    直到发现重复位置就跳出while loop即 s[right] in pool
    同时可以比较大小，打擂台的方式。
    这一个模板套路代码为:
    while right < len(s) and s[right] not in pool:
        pool.add(s[right])
        right += 1
        res = max(res, len(pool))
        
    跳出来就照顾慢指针(left)的情况，因为有重复了，所以left要向前一步。
    同时要删除left在pool里面的值，即使它并不是重复的那个。即:
    left += 1
    pool.remove(s[left])
    
    这样一直改变滑动窗口比较里面字母，知道right 走到最后。
    
    同向双指针 一般套路就是写个 while loop, 确保 right < len(nums)
    里面就是让right一直跑，直到不满足条件 跳出，nums[right] not in xxx
    开始处理，(删数据，打擂台)，然后left pointer += 1继续。
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        res = 0
        pool = set()
        
        while right < len(s):
            while right < len(s) and s[right] not in pool:
                pool.add(s[right])
                right += 1
                res = max(res, len(pool))
            
            pool.remove(s[left])
            left += 1
            
        return res


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
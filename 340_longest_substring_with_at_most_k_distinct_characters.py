class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        slow = 0
        fast = 0
        visited = {}
        res = 0
        
        '''
        同向双指针经典题目，设两个指针slow/fast, 让fast别越界的while loop
        对于当前fast的字母，如果不满足条件即 len(visited) > k, 
        则处理slow, 此处也可以写while loop 更经典。但if 即可。
        
        对于slow, 则把cnt 减一，或者删除。
        最后看当前长度和全局打擂台，即答案。
        '''
        
        while fast < len(s):
            visited[s[fast]] = visited.get(s[fast], 0) + 1
            
            if len(visited) > k:
                visited[s[slow]] -= 1
                if visited[s[slow]] == 0:
                    del visited[s[slow]]
                slow += 1
            
            res = max(res, fast - slow + 1)
            fast += 1
            
        return res
                
            
            
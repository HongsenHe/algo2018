class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #my solution, practice defaultdict, 180ms
        groups = collections.defaultdict(list)
        for i in range(len(s)):
            groups[s[i]].append(i)
        
        res = len(s)
        for v in groups.values():
            if len(v) == 1:
                if v[0] < res:
                    res = v[0]
        
        if res == len(s):
            res = -1
        
        return res
        
    
        '''
        # try to use count function, but TLE...
        for i in range(len(s)):
                c = s[i]
                if s.count(c)==1:
                    return i

        return -1
        '''

        '''
        # 684ms...
        d = {}
        for c in s:
            if c in d.keys():
                d[c] += 1
            else:
                d[c] = 1

        for i in range(len(s)):
            c = s[i]
            if d[c]==1:
                return i

        return -1 
        '''
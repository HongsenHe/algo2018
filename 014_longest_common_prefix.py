class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return "" 
        strs.sort()
        shortest = strs[0]
        # shortest = min(strs, key=len)
        for k, v in enumerate(shortest):
            for each in strs:
                if each[k] != v:
                    return shortest[:k]
        return shortest
            
        # pythonic
        #return os.path.commonprefix(strs)
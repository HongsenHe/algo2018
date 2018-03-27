class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        '''
        # solution1: using substring, time O(m+n)
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        '''

        '''
        # solution2: using internal function
        return haystack.find(needle)
        '''
        
        # solution3: using two pointers!!
        if not needle:
            return 0
        for i in range(0, len(haystack) - len(needle) + 1):
            j = 0
            while j < len(needle) and haystack[i+j] == needle[j]:
                j += 1
            if j == len(needle):
                return i
        return -1
                    
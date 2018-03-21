class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}
        
        for item in s:
            if item in dic1:
                dic1[item] += 1
            else:
                dic1[item] = 1
        
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        
        return dic1 == dic2
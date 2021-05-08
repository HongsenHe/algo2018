class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for str1 in strs:
            # how to sort a string
            str2 = ''.join(sorted(str1))
            if str2 in dic:
                dic[str2].append(str1)
            else:
                dic[str2] = [str1]
        return dic.values()


        #test
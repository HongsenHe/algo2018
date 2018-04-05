class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 每次查到一个关键字，就算一下距离，局部变量和全局变量想比较的故事
        minDis = len(words)
        idx1, idx2 = -1, -1
        
        for i in range(len(words)):
            if words[i] == word1:
                idx1 = i
            elif words[i] == word2:
                idx2 = i
                
            if idx1 != -1 and idx2 != -1:
                minDis = min(minDis, abs(idx1-idx2))
        return minDis

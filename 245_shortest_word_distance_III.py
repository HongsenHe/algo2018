class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        '''
        还是比较当前单词和目标，取index 计算距离更新最小距离神马的。
        如果这两个字相同，让两个指针相同，相当于第二个指针留在原地，然后继续走
        如果发现当前单词和目标一样，则计算距离（当前指针和刚原地指针的距离）再设相同
        '''
        
        same = word1 == word2
        idx1 = -1
        idx2 = -1
        diff = len(words)
        
        for i in range (len(words)):
            if words[i] == word1:
                idx1 = i
                if idx1 != -1 and idx2 != -1:
                    diff = min(diff, abs(idx1 - idx2))
                if same:
                    idx2 = idx1
            elif not same and words[i] == word2:
                idx2 = i
                if idx1 != -1 and idx2 != -1:
                    diff = min(diff, abs(idx1 - idx2))
        return diff
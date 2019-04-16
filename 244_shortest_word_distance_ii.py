class WordDistance:

    def __init__(self, words: List[str]):
        self.words = {}
        for i in range(len(words)):
            word = words[i]
            if word in self.words:
                self.words[word].append(i)
            else:
                self.words[word] = [i]
        
    def shortest(self, word1: str, word2: str) -> int:
        '''
        list1 = self.words[word1]
        list2 = self.words[word2]
        res = float('inf')
        for i in list1:
            for j in list2:
                res = min(res, abs(i-j))
        return res
        '''
        
        # another way time: O(N)
        list1 = self.words[word1]
        list2 = self.words[word2]
        res = float('inf')
        i, j = 0, 0
        
        # 谁小就前进一个，逐渐构成最短距离
        while i < len(list1) and j < len(list2):
            res = min(res, abs(list1[i] - list2[j]))
            if list1[i] < list2[j]:
                i += 1
            else:
                j += 1
        return res
            
        
        
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
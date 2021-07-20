class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        
        for i in range(len(order)):
            dic[order[i]] = i
            
        for i in range(len(words) - 1):
            cur_word = words[i]
            next_word = words[i + 1]
            
            res = self.helper(cur_word, next_word, dic)
            if not res:
                return False
            
        return True
            
    def helper(self, word1, word2, dic):
        # 确保单词1比单词2长，此函数返回单词1是否比单词2长
        if len(word1) < len(word2):
            return not self.helper(word2, word1, dic)
        
        idx = 0
        
        while idx < len(word2):
            # 如果单词1的当前字母比单词2的小，则符合规则，直接跳出不必循环
            if dic[word1[idx]] < dic[word2[idx]]:
                break
            # 反之违规，直接返回false
            elif dic[word1[idx]] > dic[word2[idx]]:
                return False
            idx += 1
            
        # 如果都比完了，但单词1还有字母，则返回false, 比如apple vs app
        if idx == len(word2) and idx < len(word1):
            return False
        
        return True
            
            
            
                
            
            
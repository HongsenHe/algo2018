from collections import deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        res = []
        distance = {}
        wordList.add(beginWord)
        
        '''
        先从后到前的BFS一下找到所有点到END的距离
        再用DFS 从前到后找最短距离。
        '''
        self.bfs(endWord, distance, wordList)
        self.dfs(beginWord, endWord, distance, wordList, [beginWord], res)
        
        return res
    
    def dfs(self, cur, target, distance, wordList, path, res):
        '''
        经典DFS模板
        先写跳出条件，即如果当前单词就是target了，要把当前路径放到结果集中。
        注意写法，res.append(list(path))
        
        对于当前单词的所有邻居，进行遍历。
        不同的是BFS只判断当前这一层所有邻居的情况。
        DFS要从当前邻居开始出发，一直走，走到最后返回。
        
        条件是如果邻居和当前节点并不是1，也就是不相邻，则跳过。
        标准操作: 如果满足，则放到路径中，对此邻居进行DFS. 再把此邻居弹出来。
        '''
        if cur == target:
            res.append(list(path))
            return
        
        next_words = self.get_next_words(distance, wordList, cur)
        for word in next_words:
            if distance[word] != distance[cur] - 1:
                continue
                
            path.append(word)
            self.dfs(word, target, distance, wordList, path, res)
            path.pop()
            
        
    def bfs(self, start, distance, wordList):
        distance[start] = 0
        queue = deque([start])
        
        '''
        经典BFS模板
        先把起始点放进queue中，然后找到他的邻居，即get_next_words
        对于每一个邻居，如果不在distance里 则更新邻居到起始点的距离
        如果在，算是visited过了，跳过。并且把此邻居加入到queue中。
        
        '''
        
        while queue:
            word = queue.popleft()
            next_words = self.get_next_words(distance, wordList, word)

            for next_word in next_words:
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)

    
    def get_next_words(self, distance, wordList, word):
        '''
        对于单词abc的每一个字母都进行a-z替换。比如abc, bbc, cbc, dbc
        对于每一个替换的方案如果不在wordList里就跳过。
        如果在说明是编辑距离1的单词，算是word的邻居们，放到结果中。
        
        '''
        letters = 'qwertyuioplkjhgfdsazxcvbnm'
        next_words = []
        
        for i in range(len(word)):
            for char in letters:
                if word[i] == char:
                    continue
                    
                next_word = word[:i] + char + word[i + 1: ]
                if next_word not in wordList:
                    continue
                next_words.append(next_word)
                
        return next_words
        
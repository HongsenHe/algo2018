from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # tricky part, 转化成set() 不然LTE
        wordList = set(wordList)
        queue = deque([beginWord])
        visited = set([beginWord])
        distance = 0
        
        '''
        经典BFS题
        把唯一的起始点放到queue中，然后找和他的编辑距离是1的所有节点。
        此处用了更快速的方法，即对于abc的每一个字母, 用26个字母分别代替。
        比如abc, bbc, cbc... 看是否在wordList里出现。并且看是否访问过。
        如果满足这俩条件，说明编辑距离是1，保存起来。
        
        对于每一个编辑距离为1的单词，都加入到queue中进行下一轮处理，
        并且放到visited里。
        
        每次处理都要拿一批出来，好比是这个level的所有元素。
        即 for i in range(len(queue)) 此处为通用模板。类似level order
        '''
        
        while queue:
            distance += 1
            
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return distance
    
                next_words = self.get_next_words(word, visited, wordList)
                for next_word in next_words:
                    queue.append(next_word)
                    visited.add(next_word)

        return 0
        
        
    def get_next_words(self, word, visited, wordList):
        # Time O(25 * L^2)
        letters = 'qwertyuioplkjhgfdsazxcvbnm'
        words = []
        
        # Time: O(L)
        for i in range(len(word)):
            prefix = word[:i]
            suffix = word[i + 1:]

            # Time: 25
            for char in letters:
                if word[i] == char:
                    continue
                    
                # Time: O(L)
                new_word = prefix + char + suffix
                if new_word not in wordList or new_word in visited:
                    continue
                words.append(new_word)
        
        return words
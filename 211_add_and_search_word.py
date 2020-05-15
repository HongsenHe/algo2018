class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        
        # 一样的方法，构建Trie Tree
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.is_word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        cur = self.root
        self.res = False
        
        '''
        搜寻方法分两种情况：是 '.' 还是普通的。
        1. 如果是'.' 就要遍历所有当前节点cur的孩子cur.children, 
        切记：把TrieNode放进helper方法里，即 cur.children[child]
        2. 如果是普通的字符就看是否在当前节点的孩子里，如果不在就返回不必计算了。
        如果在就继续寻找，同理把 TrieNode也就是cur.children的value放进helper
        
        既然是回溯就要维持一个pos, 来记录走到哪了要怎么返回去。
        整个大循环就是遍历word，每个字符要看Trie tree的那一层是否有答案。
        所以pos就是用来记录当前字符的位置，也就是每次获取当前字符 w = word[pos]
        
        当pos到了最后就可以判断当前字符是否是被标注word.
        这里巧妙的维持了一个全局变量，self.res 即 只有在找到答案的时候，改变它。
        如果没找到就返回默认值False就好了。
        '''
        
        def helper(cur, pos, word):
            if pos == len(word):
                if cur.is_word:
                    self.res = True
                return
            
            w = word[pos]
            if w == '.':
                for child in cur.children:
                    helper(cur.children[child], pos + 1, word)
            else:
                if w not in cur.children:
                    return
                helper(cur.children[w], pos + 1, word)

        
        helper(cur, 0, word)
        return self.res
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
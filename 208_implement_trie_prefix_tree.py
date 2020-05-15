class TrieNode:
    def __init__(self):
        '''
        对于TrieNode节点来说，有两个变量，
        一个是is_word用来标注当前节点就是单词。
        另一个就是children 来表达当前节点和孩子们的关系，这里用dict
        key就是字符（毕竟要比较和找到字符）value还是一个TrieNode 因为孩子也有孩子
        不断的构建此数据结构。对于三种方法，都需要从root节点开始找，依次走下去。
        '''
        self.is_word = False
        self.children = {}
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        
        '''
        给一个新的单词，要从root 开始查看。
        对于单词的每一个字符，如果没有存在当前节点的孩子们中，
        就把这个字符 放进当前节点的孩子们中，dict结构，key就是字符 value就是TrieNode
        然后继续走，让当前节点走下去。最后标准当前节点是个单词 即 is_word = True
        '''
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        
        cur.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        
        '''
        给一个单词，从root 开始查看
        对于每一个字符，如果找不到直接返回错。让当前节点不停走下去。
        如果到最后节点刚好是标注了单词 即 is_word = True， 就返回此结果。
        '''
        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        
        '''
        和search 方法一样，对于一个单词，如果所有都能找到，就可以返回True
        '''
        for w in prefix:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
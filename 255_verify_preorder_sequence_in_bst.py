class Solution:
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        '''
              5
             / \
            3   6
           / \
          1   4
          
          preorder = [5, 3, 1, 4, 6]
        
        按照顺序走一遍preorder，
            先设定一个最小值，如果当前节点甚至小于这个最小值是错的
        设定一个stack, 
            如果当前节点小于stack最顶元素，比如5 -> 3 -> 1 一路下跌，
                说明一直向左子树走，就把当前元素放进stack里吧。
            如果当前节点大于stack最顶元素，那么就是触底反弹！也就是开始
                往右子树走，同时要不断更新最小值low，因为每一次反弹都有
                一个新高，也就是他的root节点，并且pop出来 已经处理过了。
                最后再把这个节点放入stack里比较
        '''
        low = float('-inf')
        sk = []
        for node in preorder:
            if node < low:
                return False
            
            while sk and node > sk[-1]:
                low = sk[-1]
                sk.pop()
            sk.append(node)
        
        return True
        
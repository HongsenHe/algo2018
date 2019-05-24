# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
next()返回最小值，也就是一直向左走，即初始化的时候从root开始
一直左走，都放进stack里面。调用next()的时候，返回stack顶即可
如果返回的值有右子树，要继续把柚子树的左孩儿们放进stack，因为
下一个最小值就在其中！hasNext()就看stack是不是空啦！
'''

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.sk = []
        self.putLeft(root)
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.sk) != 0

    def next(self):
        """
        :rtype: int
        """
        res = self.sk.pop()
        if res.right:
            self.putLeft(res.right)
        return res.val
    
    def putLeft(self, root):
        while root:
            self.sk.append(root)
            root = root.left
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
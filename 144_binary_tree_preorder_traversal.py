# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # updated 05152021
    def preorderTraversal(self, root):
        res = []
        sk = []

        '''
        preorder, root 左右，看到root就马上加进res list里。
        然后移动root到left tree, 并且压入stack里。 如果到底了则弹出
        并且移动root到当前node的right tree，即root = cur.right
        
        '''
        
        
        while root or sk:
            while root:
                res.append(root.val)
                sk.append(root)
                root = root.left
                
            cur = sk.pop()
            root = cur.right
        return res
    '''
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.helper(root.left, res)
        self.helper(root.right, res)
    '''
        
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        sk = []
        while root or sk:
            if root:
                res.append(root.val)
                sk.append(root)
                root = root.left
            else:
                cur = sk.pop()
                root = cur.right
        return res
                
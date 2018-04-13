# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if not root:
            return 
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)
    '''
    def inorderTraversal(self, root):
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
                sk.append(root)
                root = root.left
            else:
                cur = sk.pop()
                res.append(cur.val)
                root = cur.right
        return res
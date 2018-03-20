# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        return self.helper(root, res)
    
    def helper(self, root, res):
        # if current node is none, just return 0
        if not root:
            return 0
        
        res = res * 10 + root.val
        # if current node is a leaf, return sum
        if not root.left and not root.right:
            return res
    
        return self.helper(root.left, res) + self.helper(root.right, res)
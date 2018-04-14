# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, float('inf'), float('-inf'))
    def helper(self, root, high, low):
        if not root:
            return True
        if root.val <= low or root.val >= high:
            return False
        return self.helper(root.left, root.val, low) and self.helper(root.right, high, root.val)
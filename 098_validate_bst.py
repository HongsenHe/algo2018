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


    # updated at 04292020
    sk = [(root, float('inf'), float('-inf'))]
        
        while sk:
            root, up, down = sk.pop()
            if not root:
                continue
                
            if root.val >= up or root.val <= down:
                return False
            
            sk.append([root.left, root.val, down])
            sk.append([root.right, up, root.val])
            
        return True
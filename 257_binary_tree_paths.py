# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if not root:
            return res
        self.helper(root, res, str(root.val))
        return res
    
    def helper(self, root, res, each):
        # exit, as current node is leaf
        if not root.left and not root.right:
            res.append(each)
            return 
        
        # adding child treeNode, not current root, otherwise init root will be added twice
        if root.left:
            self.helper(root.left, res, each + "->" + str(root.left.val)) 
        if root.right:
            self.helper(root.right, res, each + "->" + str(root.right.val))
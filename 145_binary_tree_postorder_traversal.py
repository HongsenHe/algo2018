# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(res, root)
        return res
        
    def helper(self, res, root):
        if not root:
            return
        
        self.helper(res, root.left)
        self.helper(res, root.right)     
        res.append(root.val)

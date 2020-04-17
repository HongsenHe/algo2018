# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorder(self, root):
    res = []
    if not root:
        return res
    
    sk = [root]
    
    while sk:
        root = sk.pop()
        res.insert(0, root.val)
        if root.left:
            sk.append(root.left)
        if root.right:
            sk.append(root.right)
        
    return res
    
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

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root or not p or not q:
            return root
        
        while root:
            if root.val < min(p.val, q.val):
                # root = root.right
                return self.lowestCommonAncestor(root.right, p, q)
            elif root.val > max(p.val, q.val):
                # root = root.left
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                break
                
        return root
            
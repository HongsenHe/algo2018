# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        diff = float('inf')
        res = 0
        while root:
            if abs(target-root.val) < diff:
                diff = abs(target-root.val)
                res = root.val
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return res
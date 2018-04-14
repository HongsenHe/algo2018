# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        counter = collections.Counter()
        def helper(root):
            if not root:
                return
            counter[root.val] += 1
            helper(root.left)
            helper(root.right)
        helper(root)
        maxN = max(counter.values())
        return [k for k, v in counter.items() if v == maxN]
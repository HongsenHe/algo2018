# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.helper(1, n)

    def helper(self, start, end):
        if start > end:
            return [None]
        res = []
        for rootVal in range(start, end+1):
            leftTree = self.helper(start, rootVal-1)
            rightTree = self.helper(rootVal+1, end)
            for i in leftTree:
                for j in rightTree:
                    root = TreeNode(rootVal)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res
    
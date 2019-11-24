# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        nodes = []
        if not root:
            return 0
        sk = [root]
        while sk:
            n = len(sk)
            for i in range(n):
                cur = sk.pop(0)
                if cur.left:
                    sk.append(cur.left)
                if cur.right:
                    sk.append(cur.right)
            nodes.append(n)
        return pow(2, len(nodes)-1) - 1 + nodes[-1]
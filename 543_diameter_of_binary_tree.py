# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        '''
        每次计算当前root的左右子树的长度之和和候选结果res比较
        dfs 不断更新res 并且更新当前node的深度
        '''
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(left + right, self.res)
            return 1 + max(left, right)
        dfs(root)
        return self.res

        
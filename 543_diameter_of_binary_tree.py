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

        因为答案并不一定经过根节点，所以要计算每个节点左右子树之和
        并且和一个全局变量比较。

        标准dfs问题，如果当前节点是None， 则返回0，
        分别求左右节点的长度，记得此函数是对于root来说，
        最大长度是多少，即max(left_res, right_res) + 1 (root)
        left_res = dfs(root.left)
        right_res = dfs(root.right)

        但其中要维持一个全局变量来找题目中的答案。
        '''
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(left + right, self.res)
            return 1 + max(left, right)
        dfs(root)
        return self.res

        
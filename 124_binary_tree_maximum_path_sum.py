# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        '''
        递归DFS，从下到上
        分别找左子树的sum和右子树的sum, 如果小于0 就直接给0
        还有穿过root的合集，来和max_sum比较。
        每次都返回以当前node为root的左或者右子树的合集。
        '''
        self.max_sum = float('-inf')
        self.helper(root)
        return self.max_sum
    
    
    def helper(self, root):
        if not root:
            return 0
        
        left_sum = max(self.helper(root.left), 0)
        right_sum = max(self.helper(root.right), 0)
        cross_root = root.val + left_sum + right_sum
        
        self.max_sum = max(self.max_sum, cross_root)
        
        return root.val + max(left_sum, right_sum)
    
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        '''
        有几种情况：
        在当前节点的左子树有答案，或者右子树，或者cross root
        如果左子树的值<0, 则取0，即不走左子树。同理右子树。
        最终看cross root 即root + left + right和最大值打擂台
        即self.max_sum是答案
        
        helper函数永远返回 已当前root为起点，左或右子树的集合
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
    
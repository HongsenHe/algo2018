# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0
        self.helper(root)
        return self.res
    
    
#     def helper(self, root):
#         if not root:
#             return 0
        
#         left = self.helper(root.left)
#         right = self.helper(root.right)
        
#         # 如果左右子树和 root 不相同 就重置
#         if not root.left or root.left.val != root.val:
#             left = 0
#         if not root.right or root.right.val != root.val:
#             right = 0
            
#         self.res = max(self.res, left + right)
#         return max(left, right) + 1

    # another way
    def helper(self, root):
        if not root:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        # 如果左右子树和root相同，结果要加上这个节点 +1，否则重置
        if root.left and root.left.val == root.val:
            left += 1
        else:
            left = 0
            
        if root.right and root.right.val == root.val:
            right += 1
        else:
            right = 0
        
        # 穿过此节点root的最长路径left + right 和全局结果比较
        self.res = max(self.res, left + right)
        
        # helper 函数返回的就是从此节点root 开始的最长路径
        return max(left, right)
            
        
        
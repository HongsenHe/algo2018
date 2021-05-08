# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         if abs(self.tree_height(root.left) - self.tree_height(root.right)) > 1:
#             return False
#         return self.isBalanced(root.left) and self.isBalanced(root.right)
        
#     def tree_height(self, node):
#         if not node:
#             return 0
    
#         return max(self.tree_height(node.left), self.tree_height(node.right)) + 1
    
        return self.get_height(root) != -1
    
    
    def get_height(self, node):
        if not node:
            return 0
        
        # 分治法更有效率，先求左右子树的值，divide
        left = self.get_height(node.left)
        right = self.get_height(node.right)
        
        # 再合并当前节点的左右子树的值，conquer 如果不满足条件则返回-1 用来标志unbalanced
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        
        # 最后返回当前节点的高度，即此函数的目的。
        return max(left, right) + 1
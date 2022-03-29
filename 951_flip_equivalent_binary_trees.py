# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        '''
        说是翻转之后相等，但不需要真正的翻转 left, right = dfs(right), dfs(left)
        此题参考101， symmetric tree。
        三种基本情况：如果相等，True, 如果有一个是空的，False, 如果值都不一样，必然False
        之后再返回‘翻转’的四种情况
        
        '''
        if root1 == root2:
            return True
        
        if not root1 or not root2:
            return False
        
        if root1.val != root2.val:
            return False
        
        return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) or self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
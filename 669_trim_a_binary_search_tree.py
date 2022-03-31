# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        '''
        几种基本情况
        1. 如果当前的val < low, 说明左子树都可以砍掉，因为root.left < root，即向右走
        2. 如果当前的val > high, 说明右子树都可以砍掉，root.right > root，向左走

        如果not root, return就好
        分治法，分别求root.left 和root.right, 最后返回当前root在trim之后的结果
        
        '''
        
        if not root:
            return
        if root.val < low:
            # too small, should go right
            return self.trimBST(root.right, low, high)
        if root.val > high:
            # too big, should go left
            return self.trimBST(root.left, low, high)
        
        # trimming,,,and get result
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
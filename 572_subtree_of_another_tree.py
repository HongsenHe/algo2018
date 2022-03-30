# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        此题的基础是 判断两个树是sameTree, 参考第100题。
        可以在isSubtree直接写递归，即如果有一个是空的，则返回False, 
        如果两个都是空的，是True，但接下来的 isSameTree已经包含这种情况了
        所以不予考虑。
        
        如果root和subRoot不同，则考虑root的左右子树是否与subRoot相同
        一直顺眼查找，如果能找到其子树与subRoot相同即是答案，如果都找不到则False
        '''
        if not root or not subRoot:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
    def isSameTree(self, p, q):
        # code from No.100
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.res = 0
        if root:
            self.helper(root, root.val)
        return self.res
    
    '''
    分别求left, right的subtree情况，如果都符合，即子树都等于cur, 结果+1
    如果cur 还和父节点相等，则返回True，说明此节点也可以保留作为结果
    '''
    def helper(self, cur, prev):
        if not cur:
            return True
        
        left = self.helper(cur.left, cur.val)
        right = self.helper(cur.right, cur.val)
        
        if left and right:
            self.res += 1
            if cur.val == prev:
                return True
        return False
        
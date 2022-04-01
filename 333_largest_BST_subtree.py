# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SubTree():
    def __init__(self, largest, n, min, max):
        self.largest = largest  
        self.n = n               
        self.min = min          
        self.max = max  
        
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        # 检验每个node, 如果是就看节点的个数, from ch9
        res = self.dfs(root)
        return res.largest
    
    def dfs(self, root):
        if not root:
            return SubTree(0, 0, float('inf'), float('-inf'))
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        if root.val > left.max and root.val < right.min:  # valid BST
            n = left.n + right.n + 1
        else:
            n = float('-inf')
            
        largest = max(left.largest, right.largest, n)
        return SubTree(largest, n, min(left.min, root.val), max(right.max, root.val))
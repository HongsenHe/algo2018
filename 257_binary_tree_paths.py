# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return None
        res = []
        self.dfs(root, res, [str(root.val)])
        return res
    
    def dfs(self, root, res, path):
        if not root.left and not root.right:
            path_str = '->'.join(path)
            res.append(path_str)
            return
        
        if root.left:
            path.append(str(root.left.val))
            self.dfs(root.left, res, path)
            path.pop()
            
        if root.right:
            path.append(str(root.right.val))
            self.dfs(root.right, res, path)
            path.pop()
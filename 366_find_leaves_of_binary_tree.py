# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if not root:
            return -1
        
        height = -1
        
        # 当前高度取决于左右子树最大值
        height = max(height, self.helper(root.left, res) + 1)
        height = max(height, self.helper(root.right, res) + 1)
        
        # 如果res有一个list，代表第一层, 即len(res) = 1, 如果当前高度>=
        # res里面的层数了，需要再增加层数，即append([]), 并且把当前作为起点加入
        if height >= len(res):
            res.append([])
            
        res[height].append(root.val)
        
        return height
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.helper(root, sum, [], res)
        return res
    
    def helper(self, root, target, each, res):
        if not root:
            return
        # everytime, put current node into each res, but may not be in final res
        each.append(root.val)

        # if current node is a leaf, and value == target, put into res
        if not root.left and not root.right and root.val == target:
            res.append(list(each))
        else:    
            # if current node is not a leaf, keep going its children
            self.helper(root.left, target - root.val, each, res)
            self.helper(root.right, target - root.val, each, res)
        
        # as we always put cur node into each res, if not the answer, pop out
        each.pop()
            
        
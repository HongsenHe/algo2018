# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        return self.helper(root, arr, 0)
        
    
    def helper(self, root, arr, pos):
        if not root or pos == len(arr):
            return False
        
        if pos == len(arr) - 1 and not root.left and not root.right and root.val == arr[pos]:
            return True
        
        if root.val != arr[pos]:
            return False
        return self.helper(root.left, arr, pos+1) or self.helper(root.right, arr, pos+1)
        
        
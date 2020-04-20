# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        '''
        # solution 1: Time O(nlgn), Space O(n)
        inorder = sorted(preorder)
        return self.helper(preorder, inorder)
    
    
    def helper(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder.pop(0))
        idx = inorder.index(root.val)
        
        root.left = self.helper(preorder, inorder[:idx])
        root.right = self.helper(preorder, inorder[idx+1:])
        return root
        '''
        
        # solution 2: Time O(n), Space. O(n)
        return self.helper(float('-inf'), float('inf'), preorder)
    
    
    def helper(self, lower, upper, preorder):
        if not preorder:
            return None
        
        # test first, if valid, then pop
        val = preorder[0]
        if val < lower or val > upper:
            return None
        
        root = TreeNode(preorder.pop(0))
        root.left = self.helper(lower, val, preorder)
        root.right = self.helper(val, upper, preorder)
        
        return root

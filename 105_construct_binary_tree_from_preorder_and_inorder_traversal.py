# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        
        '''
        一样的原理，根据preorder的顺序：root left right 来构造root
        和子树的关系，从inorder里找到
        '''
        root = TreeNode(preorder.pop(0))
        idx = inorder.index(root.val)
        
        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])
        
        return root
        
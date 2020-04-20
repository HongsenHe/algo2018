# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        '''
        preorder: root, left, right    
        postorder: left, right, root
        '''
        self.pre_idx = 0
        self.post_idx = 0
        
        return self.helper(pre, post)
    
    def helper(self, pre, post):
        root = TreeNode(pre[self.pre_idx])
        self.pre_idx += 1
        
        if root.val != post[self.post_idx]:
            root.left = self.helper(pre, post)
        if root.val != post[self.post_idx]:
            root.right = self.helper(pre, post)
            
        self.post_idx += 1
        return root
            
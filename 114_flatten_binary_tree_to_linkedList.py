# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        if root.left:
            self.flatten(root.left)
        if root.right:
            self.flatten(root.right)
            
        '''
             1
            / \
           2   5
          / \   \
         3   4   6

             1
            / \
           2   5
            \   \
             3   6
              \    
               4

           1
            \
             2
              \
               3
                \
                 4
                  \
                   5
                    \
                     6
            
        1. 保留 root.right (4) 一会使用
        2. root的left 变成 root的right, 比如3变成2的right tree
        3. 同时reset left tree
        4. 一直走，找到最右子树 while loop
        5. 把刚保留的 4 变成root.right (3)的右子树
        
        用这个操作对于每一个root.left和right子树。
        
        
        '''
        tmp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = tmp
        
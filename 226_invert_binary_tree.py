# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


    # 05152021

        ************ another solution ************

        if root:
            # you have to put it in one line
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root


        ************ another solution ************

        if not root:
            return
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        
        return root




        ************ another solution ************
        if not root:
            return None
        
        queue = []
        queue.append(root)
        
        while queue:
            cur = queue.pop()
            cur.left, cur.right = cur.right, cur.left
            
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
                
        return root
            
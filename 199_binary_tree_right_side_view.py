# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        
        queue = deque([root])
        res = []
        
        while queue:
            n = len(queue)
            last_node = ''
            
            for i in range(n):
                cur = queue.popleft()
                
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                    
                last_node = cur.val
                
            res.append(last_node)
            
        return res
        
        
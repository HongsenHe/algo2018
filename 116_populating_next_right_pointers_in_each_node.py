"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        q = []
        q.append(root)
        
        while q:
            size = len(q)
            
            for i in range(size):
                cur = q.pop(0)
                # do not point the last node
                if i < size - 1:
                    cur.next = q[0]
                
                # enqueue children
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return root
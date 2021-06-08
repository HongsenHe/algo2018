"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        left_head = self.treeToDoublyList(root.left)
        right_head = self.treeToDoublyList(root.right)
        root.left = root
        root.right = root
        
        left = self.connect(left_head, root)
        return self.connect(left, right_head)
    
    def connect(self, node1, node2):
        if not node1:
            return node2
        if not node2:
            return node1
        
        tail1 = node1.left
        tail2 = node2.left
        
        tail1.right = node2
        node2.left = tail1
        tail2.right = node1
        node1.left = tail2
        
        return node1


        

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        self.head = None
        self.prev = None
        
        if not root:
            return None
        
        self.helper(root)
        self.prev.right = self.head
        self.head.left = self.prev
        return self.head
    
    def helper(self, node):
        if not node:
            return
        
        self.helper(node.left)
        if self.prev:
            node.left = self.prev
            self.prev.right = node
        else:
            self.head = node
        self.prev = node
        self.helper(node.right)
        
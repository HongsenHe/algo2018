# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
#         if not root:
#             return None
        
#         # key is the original node, value is the copied node
#         copy = {}
#         stack = [root]

#         # step 1: make a copy of each node
#         while stack:
#             node = stack.pop()
#             # create a new node using NodeCopy
#             copy[node] = NodeCopy(node.val)
            
#             # DFS way, trasveral each node
#             if node.left:
#                 stack.append(node.left)
#             if node.right:
#                 stack.append(node.right)
                
#         # step 2: connect each copied node
#         stack = [root]
        
#         while stack:
#             node = stack.pop()
#             if node.left:
#                 copy[node].left = copy[node.left]
#                 stack.append(node.left)
#             if node.right:
#                 copy[node].right = copy[node.right]
#                 stack.append(node.right)
#             if node.random:
#                 copy[node].random = copy[node.random]

#         return copy[root]

        # another way
        copy = {}
        
        def dfs(root):
            if not root: 
                return None
            
            if root in copy:
                return copy[root]
            
            cp_root = NodeCopy(root.val)
            copy[root] = cp_root
            cp_root.left = dfs(root.left)
            cp_root.right = dfs(root.right)
            cp_root.random = dfs(root.random)
            
            return cp_root
        
        return dfs(root)
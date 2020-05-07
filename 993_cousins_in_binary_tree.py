# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [root]
        while queue:
            level = {}
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    level[node.left.val] = node
                if node.right:
                    queue.append(node.right)
                    level[node.right.val] = node
            
            # same level, but different parent. 
            if x in level and y in level and level[x] != level[y]:
                return True
        return False
        
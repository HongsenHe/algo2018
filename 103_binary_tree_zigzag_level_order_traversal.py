# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        
        queue = collections.deque([root])
        reverse = False
        res = []
        
        while queue:
            n = len(queue)
            level = []
            
            for i in range(n):
                cur_node = queue.popleft()
                level.append(cur_node.val)
            
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            
            if reverse:
                level.reverse()
                reverse = False
            else:
                reverse = True
                
            res.append(level)
            
        return res

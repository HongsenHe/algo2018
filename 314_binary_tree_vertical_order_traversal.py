# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = collections.defaultdict(list)
        queue = collections.deque()
        queue.append((root, 0))
        
        '''
        把每个node都编号，当前root = a, root.left = a - 1, root.right = a + 1
        因为左孩子在前一个column, 即a - 1
        
        用经典level order (BFS) 来撸一遍所有node， 注意使用defaultdict(list)的写法
        然后再按照编号排序，每个编号应该对应一串node, 即当前col的所有node
        
        '''
        
        
        while queue:
            node, col_idx = queue.popleft()
            
            if node:
                res[col_idx].append(node.val)
                queue.append((node.left, col_idx - 1))
                queue.append((node.right, col_idx + 1))
                
        return [res[i] for i in sorted(res)]
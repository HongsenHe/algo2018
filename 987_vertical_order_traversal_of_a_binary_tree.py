# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_nodes = collections.defaultdict(list)
        queue = collections.deque()
        queue.append((root, 0))
        
        '''
        把每个node都编号，当前root = a, root.left = a - 1, root.right = a + 1
        因为左孩子在前一个column, 即a - 1
        
        用经典level order (BFS) 来撸一遍所有node， 注意使用defaultdict(list)的写法
        然后再按照编号排序，每个编号应该对应一串node, 即当前col的所有node
        
        注意和314题不一样的地方。
        '''
        level = 0
        
        while queue:
            for _ in range(len(queue)):
                node, col_idx = queue.popleft()

                if node:
                    col_nodes[col_idx].append((node.val, level))
                    queue.append((node.left, col_idx - 1))
                    queue.append((node.right, col_idx + 1))
            level += 1
            
        # 和314题不一样的地方。
        res = []
        for col_node in sorted(col_nodes):
            col_nodes[col_node].sort(key=lambda x: (x[1], x[0]))
            res.append([x[0] for x in col_nodes[col_node]])
            
        return res

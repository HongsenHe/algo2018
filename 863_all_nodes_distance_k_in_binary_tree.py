# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 构建当前节点的父节点
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        # 经典BFS算法，找到第k层的时候，所有节点即是答案
        queue = collections.deque([(target, 0)])
        seen = {target}
        
        while queue:
            # 找到了第k层
            if queue[0][1] == k:
                return [node.val for node, d in queue]
            
            node, d = queue.popleft()
            
            # 当前节点node的所有邻居（类似于图）是父节点，左右子节点
            for neighbour in (node.left, node.right, node.par):
                if neighbour and neighbour not in seen:
                    seen.add(neighbour)
                    queue.append((neighbour, d+1))

        return []
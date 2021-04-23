from collections import deque

DIRECTIONS = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        '''
        所谓的从起点到终点的最短距离，就用BFS
        因为此搜索是按照雷达的方式，一层一层的找答案，找到了肯定就是从起始点的最短路径。
        '''
        
        # 创建一个queue 并且加入起始点，此题从坐标(0, 0)开始
        queue = deque([(0, 0)])
        
        # 此distance表示每个点距离起始点的距离, 并且可以当做visited用
        distance = {(0, 0) : 0}
        
        while queue:
            cur_x, cur_y = queue.popleft()
            
            # 如果找到了直接返回答案。
            if (cur_x, cur_y) == (x, y):
                return distance[(cur_x, cur_y)]
            
            # 套路就是每次弹出来一个点，都找他的邻居，在grid这种问题中，就走接下来的directions
            for dir_x, dir_y in DIRECTIONS:
                next_x = cur_x + dir_x
                next_y = cur_y + dir_y
                neighbor = (next_x, next_y)
                
                if neighbor in distance:
                    continue
                    
                # 更新这个邻居节点 neighbor 到当前节点 cur_x, cur_y的距离 + 1
                distance[neighbor] = distance[(cur_x, cur_y)]+ 1
                
                # 把当前节点的邻居也加入queue中。
                queue.append(neighbor)
                
        return -1
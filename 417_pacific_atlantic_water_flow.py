from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_queue = set()
        atlantic_queue = set()
        
        '''
        从海洋反推陆地的BFS经典问题。
        推两遍：如果从pacific到陆地有路径，并且atlantic也有路径，则是答案
        用经典BFS模板，找到所有沿海城市作为起点放入queue
        
        弹出一个沿海城市作为起点，搜索四个方向，如果越界了，访问过了，或者新的城市更矮
        则略过，如果满足调节剂，把新的城市加入visited/queue
        
        出来的结果是一条路径，合并两个路径即是答案。
        
        '''
        
        
        m = len(heights)
        n = len(heights[0])
        
        # 从pacific 来的格子，即第一列和第一行，从atlantic来，最后一列，最后一行
        for i in range(m):
            pacific_queue.add((i, 0))
            atlantic_queue.add((i, n - 1))
            
        for j in range(n):
            pacific_queue.add((0, j))
            atlantic_queue.add((m - 1, j))
            
        pacific_visited = self.bfs(pacific_queue, heights)
        atlantic_visited = self.bfs(atlantic_queue, heights)
        
        return list(pacific_visited & atlantic_visited)
    
    def bfs(self, starts, heights):
        m = len(heights)
        n = len(heights[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque(list(starts))
        visited = set(list(starts))
        
        while queue:
            orig_x, orig_y = queue.popleft()
        
            for dir_x, dir_y in dirs:   
                cur_x = orig_x + dir_x
                cur_y = orig_y + dir_y
                
                if cur_x < 0 or cur_x > m - 1 or cur_y < 0 or cur_y > n - 1:
                    continue
                    
                if (cur_x, cur_y) in visited:
                    continue
                    
                # 新的方向比起点矮，则不考虑
                if heights[cur_x][cur_y] < heights[orig_x][orig_y]:
                    continue
                    
                visited.add((cur_x, cur_y))
                queue.append((cur_x, cur_y))
            
        return visited
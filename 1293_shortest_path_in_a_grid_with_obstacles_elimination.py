from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        start = (0, 0, grid[0][0])
        queue = deque([start])
        visited = set([start])
        steps = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(grid) - 1
        n = len(grid[0]) - 1
        
        '''
        一样的配方BFS模板。只是多了一个obstacles看看是否能消除<=k块
        起始点是(0, 0, 0) 代表(0, 0)坐标，已经消除了0块。
        放入queue中进行while loop
        
        *此处使用for queue， 为了找到当前的答案？
        
        其他都是标准模板：搜四个方向，如果越界了，skip 
        更新obs（如果当前是0，则不变，如果是数字则+1，但保证new_obs <= k)
        如果找到答案则返回，如果都满足，则放到visited/queue
        
        
        '''
        
        while queue:
            for i in range(len(queue)):
                orig_x, orig_y, obs = queue.popleft()

                if (orig_x, orig_y) == (m, n):
                    return steps

                for dir_x, dir_y in dirs:
                    cur_x = orig_x + dir_x
                    cur_y = orig_y + dir_y

                    if cur_x < 0 or cur_x > m or cur_y < 0 or cur_y > n:
                        continue

                    new_obs = obs + grid[cur_x][cur_y]
                    new_node = (cur_x, cur_y, new_obs)

                    if new_obs <= k and new_node not in visited:
                        visited.add(new_node)
                        queue.append(new_node)
            
            steps += 1
            
        return -1
                
            
            
        
        
        
        
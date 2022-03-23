from collections import deque

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        queue = deque([(start[0], start[1])])
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        visited = set()
        
        while queue:
            # 弹出来当前坐标
            orig_x, orig_y = queue.popleft()
            visited.add((orig_x, orig_y))
            
            # 此处可以这样写，因为每次都走到撞墙并且放入queue里，所以如果撞墙了并且等于结果，即找到
            if (orig_x, orig_y) == (destination[0], destination[1]):
                return True
            
            # BFS搜图标准写法，loop四个方向
            for dir_x, dir_y in dirs:
                # 每次都从当前的original node开始。看四个方向，所以用cur_x, cur_y来表示当前坐标
                cur_x, cur_y = orig_x, orig_y
                cur_x += dir_x
                cur_y += dir_y
                
                # 此题不同之处，一直走，到撞墙位置，略过已走过的坐标visited
                while self.is_valid(maze, cur_x, cur_y):
                    cur_x += dir_x
                    cur_y += dir_y
                        
                # 撞墙之后要回来，回到之前状态
                cur_x -= dir_x
                cur_y -= dir_y
                
                if maze[cur_x][cur_y] == 0 and (cur_x, cur_y) not in visited:
                    # 标准写法，把当前方向（撞墙前）的坐标写入queue里
                    queue.append((cur_x, cur_y))

        return False
                
    def is_valid(self, maze, x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0                
        
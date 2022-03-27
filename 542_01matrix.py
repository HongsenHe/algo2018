from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        m = len(mat)
        n = len(mat[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        
        '''
        BFS标准题，要注意把什么放入queue中，此题把所有的0放入queue作为起点
        并且把其他元素标志为-1
        
        每次弹出来当前坐标，四个方向搜索。
        如果越界了，skip, 如果已经访问过了，即其值>=0了，初始是-1， skip
        如果满足条件，则更新其值，用弹出来的坐标 + 1个距离单位即可。
        最后把刚更新的坐标加入queue中，继续运算。
        
        '''
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1
        
        while queue:
            orig_x, orig_y = queue.popleft()
            
            for dir_x, dir_y in dirs:
                cur_x = orig_x + dir_x
                cur_y = orig_y + dir_y
                
                if cur_x < 0 or cur_x > m - 1 or cur_y < 0 or cur_y > n - 1:
                    continue
                
                if mat[cur_x][cur_y] >= 0:
                    continue

                mat[cur_x][cur_y] = mat[orig_x][orig_y] + 1
                queue.append((cur_x, cur_y))
                
        return mat
        
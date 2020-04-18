class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
#         '''
#         DFS的方法，每次搜索gate (val=0)， 如果找到 gate 就搜他的4个邻居
#         并且每个邻居和这个gate的距离val都+1
#         rooms只有三种类型，-1， 0 和INF, 如果是0 我们就作为起点搜索
#         如果是-1 就是死路，返回退出，因此只改变room是INF的数值，即和gate的距离。
#         如果之前被搜索过，并且有距离，而且比当前的小，即rooms[i][j] < val
#         则退出，比如rooms[2][3] 从gate1的距离比gate2距离近，则不需要更新。
#         '''
#         for i in range(len(rooms)):
#             for j in range(len(rooms[0])):
#                 if rooms[i][j] == 0:
#                     self.dfs(i, j, rooms, 0)
                    
#         return rooms
    
    
#     def dfs(self, i, j, rooms, val):
#         # rooms[i][j] < val means current value is -1, or previous result is shorter, ignore,
#         if i < 0 or i > len(rooms)-1 or j < 0 or j > len(rooms[0])-1 or rooms[i][j] < val:
#             return
        
#         # val is the distance from the gate (0), everytime call dfs, val += 1
#         rooms[i][j] = val
#         self.dfs(i+1, j, rooms, val+1)
#         self.dfs(i-1, j, rooms, val+1)
#         self.dfs(i, j-1, rooms, val+1)
#         self.dfs(i, j+1, rooms, val+1)
        
        '''
        BFS的方法，还是从每个gate(room[i][j]==0) 开始搜索他的四个邻居，并且放到queue中。
        每次enqueue都要把距离+1，放满之后就dequeue,如果符合资格（不越界，当前是INF room)
        就继续放这个room的四个邻居，每次也都距离+1，直到queue空虚了。
        '''
        q = collections.deque([])
        inf = (1 << 31) - 1
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))
                    
        while q:
            x, y, val = q.popleft()
            if x > 0 and rooms[x-1][y] == inf:
                rooms[x-1][y] = val+1
                q.append((x-1, y, val+1))
            if x < len(rooms)-1 and rooms[x+1][y] == inf:
                rooms[x+1][y] = val+1
                q.append((x+1, y, val+1))
            if y > 0 and rooms[x][y-1] == inf:
                rooms[x][y-1] = val+1
                q.append((x, y-1, val+1))
            if y < len(rooms[0])-1 and rooms[x][y+1] == inf:
                rooms[x][y+1] = val+1
                q.append((x, y+1, val+1))
                
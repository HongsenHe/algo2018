from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        此题本质是在图中找个环。如果有环当然无法先修某个课，造成死循环。
        难点在于构建图: 点与边的集合，入度的集合。
        
        经典BFS模板
        1. 用collections.deque() 创建queue
        2. 首先把所有入度为0的点加进queue中。
        3. 弹出来，并且看他的邻居们的状态，此时邻居的入度要减去1。
        4. 如果当前邻居的入度是0, 放进queue中继续处理。
        5. 如果弹出来的个数等于numCourses, 则跑完全程没有环。
        
        '''
        
        # 初始化构建点的集合, 用邻接表的思想(dict)。key是任意一点，value是这个点的邻居们
        edges = {i : [] for i in range(numCourses)}
        
        # 构建入度的集合，先初始化
        degrees = [0 for i in range(numCourses)]
        
        # 再加入具体点和邻居的关系，并且对于每一个点计算in degree
        for out_degree, in_degree in prerequisites:
            edges[in_degree].append(out_degree)
            degrees[out_degree] += 1
            
        # 此处开始经典BFS模板
        queue = deque()
        count = 0
        
        # BFS的第一层，先把入度为0的所有点加进去。
        for course in range(numCourses):
            if degrees[course] == 0:
                queue.append(course)
            
        # always this condition
        while queue:
            cur = queue.popleft()
            '''
            弹出来一个，则找到一个全新的节点
            如果有环，比如 0 -> 1, 2 -> 1, 1 -> 2
            则一开始把0放进queue, 但1的入度并不是0，因为2也指向1
            此时的count 只是1，但numCourses是3
            '''
            count += 1
            
            # 对于当前点的所有邻居进行操作，即入度减1
            for neighbor in edges[cur]:
                degrees[neighbor] -= 1
                
                # 如果当前点的入度是0，则加入queue中，进行下一层计算。
                if degrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        return count == numCourses
                
                
            
            
        
                    
                    
        
        
        
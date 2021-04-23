from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 构建邻接表和每个点的入度关系，初始化
        edges = {i : [] for i in range(numCourses)}
        degrees = [0 for i in range(numCourses)]
        
        # 添加数据
        for out_degree, in_degree in prerequisites:
            edges[in_degree].append(out_degree)
            degrees[out_degree] += 1
        
        queue = deque()

        # 把所有入度为0的节点放进queue, 作为第一层遍历
        for course in range(numCourses):
            if degrees[course] == 0:
                queue.append(course)
        
        order = []
        
        # 经典BFS
        while queue:
            # 弹出来一个，马上加入结果集或者访问集
            cur = queue.popleft()
            order.append(cur)
            
            # 开始遍历当前节点的每一个邻居
            for neighbor in edges[cur]:
                # 当前邻居的入度都减1，直到为0，即成为起始点，加入queue计算
                degrees[neighbor] -= 1
                
                if degrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        # 判断是否有环，如果没有，则返回order
        if len(order) == numCourses:
            return order
        
        return []
            
            
        
        
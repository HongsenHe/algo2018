class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 两个经典构建图的模板
        # 1. k = 列出所有点 v = 其孩子节点(list)
        edges = {i: [] for i in range(numCourses)}
        
        # 2. 初始所有点的入度
        degrees = [0 for i in range(numCourses)]
        
        # 构建edges: 每个节点之间的关系
        # 构建degrees: 每个节点的入度
        for k, v in prerequisites:
            # 把孩子们加入父节点的list中
            edges[v].append(k)
            # 相应节点的入度要增加
            degrees[k] += 1
            
        # 经典BFS
        import queue
        queue = queue.Queue(maxsize = numCourses)
        count = 0
        
        # 把入度是0 即起始点 加入queue
        for i in range(numCourses):
            if degrees[i] == 0:
                queue.put(i)
        
        while not queue.empty():
            node = queue.get()
            count += 1 # 弹出来一个，找到了一个
            
            for each in edges[node]:
                # 因为当前的节点少了一个父节点（node) 所以入度减一
                degrees[each] -= 1
                
                # 调整之后如果当前节点入度是0，即初始点，放进queue
                if degrees[each] == 0:
                    queue.put(each)
        
        # 如果构建之后，没有环，那么结果应该和课程数量相等
        return count == numCourses                
        
        
            
        
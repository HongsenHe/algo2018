class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        # numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        
        # {0: [], 1: [], 2: [], 3: []}
        edges = {i: [] for i in range(numCourses)}

        # [0, 0, 0, 0]
        degrees = [0 for i in range(numCourses)]

        # 构造节点之间的关系和计算入度
        for i, j in prerequisites:
            # key是父节点，value是孩子节点
            # {0: [1, 2], 1: [3], 2: [3], 3: []}
            edges[j].append(i)

            # 每当找到一个点是被指向的，说明他依赖一个别的节点，
            # 所以就增加一个度。 起始点入度是0
            # [0, 1, 1, 2]
            degrees[i] += 1

        # 经典BFS 走起！
        import Queue
        queue = Queue.Queue(maxsize = numCourses)

        for i in range(numCourses):
            # 先计算所有入度是0的点，意味着他们都是起始点
            # 放到Queue里面，开始经典BFS套路！
            if degrees[i] == 0:
                queue.put(i)

        order = []

        while not queue.empty():
            # 弹出来一个初始点，在此基础上算他的孩子节点
            node = queue.get()
            # 因为是初始点，所以可以放到result set里面
            order.append(node)

            # 计算初始点所有的孩子节点
            for x in edges[node]:
                # 因为孩子节点少了一个父亲，就是刚才的初始点
                # 所以孩子的入度要减去一
                degrees[x] -= 1

                # 同理在入度减去一之后，如果孩子的入度是0
                # 那么孩子就是初始点了，也要加进Queue
                if degrees[x] == 0:
                    queue.put(x)

        # 方式环的问题
        if len(order) == numCourses:
            return order

        return []
        
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: 
            return [0]
        '''
        此题为无向图，所以在创建queue的时候，要把入度为1的叶子节点加入。
        用剥洋葱的方式，从所有叶子节点出发，一直到有1或者2个节点即使答案。
        
        可以想成：从哪个点出发到中心（1-2个节点）可以得到最小半径的问题（高度最小）
        
        '''

        graph = defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
            
        # 因为是无向图，所以把初始入度为1的叶子加进去
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
                
        while n > 2:
            '''
            剥洋葱的方式，每次都减少当前入度为1的叶子数量
            比如  一共6个节点，初始叶子是5， 0， 1， 2，一共4个
            剩下就是3, 4两个节点作为图中心点，即答案。
            如果剩下3个节点，(1-2-3) 则可以继续剥洋葱，则2是答案
            如果剩下1个节点，则是答案（无法继续啵）
            
            所以while loop最终跳出是 剩下<=2个节点
            '''
            n -= len(leaves)
            new_leaves = []
            
            # 对于每个入度为1的叶子节点，看它的邻居是否满足入度为1
            # 如果满足，则加入queue，并且删去，不重复计算。
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
                    
            leaves = new_leaves
            
        return leaves
                
            
class Solution:
    # from ch9
    def alienOrder(self, words):
        graph = self.build_graph(words)
        if not graph:
            return ""
        return self.topological_sort(graph)
        
    def build_graph(self, words):
        # key is node, value is neighbors
        graph = {}

        # initialize graph
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set() 

        # add edges        
        n = len(words)
        for i in range(n - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break
                if j == min(len(words[i]), len(words[i + 1])) - 1:
                    if len(words[i]) > len(words[i + 1]):
                        return None
                
        return graph

    def topological_sort(self, graph):        
        # initialize indegree 
        indegree = {
            node: 0
            for node in graph
        }
        
        # calculate indegree
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] = indegree[neighbor] + 1
        
        # use heapq instead of regular queue so that we can get the 
        # smallest lexicographical order
        queue = [node for node in graph if indegree[node] == 0]
        heapify(queue)
        
        # regular bfs algorithm to do topological sorting
        topo_order = ""
        while queue:
            node = heappop(queue)
            topo_order += node
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heappush(queue, neighbor)
            
        # if all nodes popped
        if len(topo_order) == len(graph):
            return topo_order
        
        return ""
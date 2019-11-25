# copy from somewhere, Amazon OA
from collections import defaultdict
class Solution(object):
                
    def tarjan(self, graph, pre, low, parent, node):
        pre[node] = 0 if parent is None else pre[parent] + 1
        low[node] = pre[node]
        for neighbor in graph[node]:
            if neighbor not in pre:
                self.tarjan(graph, pre, low, node, neighbor)
            if neighbor != parent:
                low[node] = min(low[node], low[neighbor])
        
    
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        
        graph = defaultdict(list)
        for c in connections:
            graph[c[0]].append(c[1])
            graph[c[1]].append(c[0])
        nodes = graph.keys()
        
        pre = dict()
        low = dict()        
        self.tarjan(graph, pre, low, None, nodes[0])
        return [c for c in connections if low[c[0]] > pre[c[1]] or low[c[1]] > pre[c[0]]]
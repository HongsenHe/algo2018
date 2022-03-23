from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        用adjacent list来表示图，无向图，所以key是一个节点，value是个list，连接它的所有节点
        一共有n个节点，从0开始，如果遇到就放到visited里，表示这一批的所有节点。
        下一批（next for loop)再遇到就略过，否则是另一批(another component) 的节点
        '''
        
        graph = defaultdict(list)

        for k, v in edges:
            graph[k].append(v)
            graph[v].append(k)
            
        visited = set()
        res = 0
        
        for i in range(n):
            # 如果当前节点i 已经访问过了，则节点i属于其他component，继续
            if i in visited:
                continue
            else:
                # 如果当前节点没有访问过，则i即是新连通块的root, 继续造。。
                res += 1
                visited.add(i)
                self.bfs(visited, i, graph)
                
        return res
    
    
    def bfs(self, visited, root, graph):
        '''
        纯BFS模板，把root放进queue中，while queue。
        pop出来，看是否访问过（是否已经属于其他连通块了）
        如果没有，放到visited/queue继续弄。。。
        
        '''
        queue = deque([root])
        
        while queue:
            cur_node = queue.popleft()
            
            for neighbor in graph[cur_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                
            
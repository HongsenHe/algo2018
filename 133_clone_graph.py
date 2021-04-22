"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

# 04222021

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        # find all original nodes
        nodes = self.find_orig_nodes(node)
        # copy nodes
        mapping = self.copy_nodes(nodes)
        # copy edges
        self.copy_edges(nodes, mapping)
        
        return mapping[node]
    
    def find_orig_nodes(self, node):
        queue = deque([node])
        visited = set()
        visited.add(node)
        
        '''
        标准BFS模板
        1. 先创建个queue和visited, 并且把root node起始点放进去
        2. 再写个while queue
        3. 首先pop出来一个node
        4. 对于这个node的邻居们进行操作
        5. 如果访问过了，怎样。如果没有加进queue待处理，并且加进visited
        
        '''
        while queue:
            cur = queue.popleft()
            
            for neighbor in cur.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
                
        return list(visited)
    
    def copy_nodes(self, nodes):
        '''
        创建个map, 即映射原node和新node的关系。
        目前已知只有原nodes, 所以for loop 原nodes
        既然是新node 就要创建一个新的，即 Node(node.val)
        '''
        mapping = {}
        for node in nodes:
            mapping[node] = Node(node.val)
        
        return mapping
    
    def copy_edges(self, nodes, mapping):
        '''
        copy original node's edges, 
        so the for loop starts from the original node
        复制原node的边，也就是把邻居们的关系整合。
        
        既然是复制, 还是从原nodes开始写个for loop
        对于他的所有邻居们，先从mapping里找到当前邻居的复制品, 即
        new_neighbor = mapping[neighbor]
        然后把这个邻居加到新node的邻居集, 即
        new_node.neighbors.append(new_neighbor)
        
        '''
        for node in nodes:
            new_node = mapping[node]
            
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
    
    
    
    
    


    """
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        '''
        DFS标准模板
        1. 一个clone_map 代表原node和克隆node的关系，比如visited set()
        2. 边界条件：如果当前node是空，则返回，如果已经在map里就返回clone的node
        3. 开始递归：建造clone_node, 分两个条件一个是val 即原node.val
        另一个就是node的邻居，也是通过原node的邻居来构建，这就是用了递归，
        把每个原邻居放进函数里，返回的都是其克隆邻居，一直到空，满足边界条件返回。
        也就是走到了最深只能返回路径，同时剪个枝，即DFS
        '''
        clone_map = {}
        return self.helper(clone_map, node)
        
        
    def helper(self, clone_map, node):
        if not node:
            return None
        
        if node in clone_map:
            return clone_map[node]
        
        # init: clone node's neighbour is empty
        clone_neighbors = []
        clone_node = Node(node.val, clone_neighbors)
        clone_map[node] = clone_node
        
        for neighbor in node.neighbors:
            clone_neighbor = self.helper(clone_map, neighbor)
            clone_neighbors.append(clone_neighbor)

        return clone_node


#     def cloneGraph(self, node: 'Node') -> 'Node':
#         '''
#         BFS 方法
#         1. 创建visited or clone_map 用来表示关系，创建queue
#         2. 把start_node 放进queue里，循环queue，一个个弹出计算
#         3. 弹出一个元素cur，对于他的邻居，如果不在clone_map里，则创建一个新的
#            元素，作为克隆邻居，同时把原邻居放进queue中。
#         4. 再build 克隆元素node和克隆邻居的关系：
#            clone_map[cur]就是克隆的node, 在for loop中，每次都把克隆的邻居
#            append到这个克隆node的邻居们中。
#         5. 最后返回的就是克隆start_node, 即clone_map[node]        
#         '''
        
#         if not node:
#             return None
        
#         queue = [node]
#         clone_map = {}
#         clone_map[node] = Node(node.val, [])
        
#         while queue:
#             cur = queue.pop(0)
            
#             for neighbor in cur.neighbors:
#                 if neighbor not in clone_map:
#                     clone_map[neighbor] = Node(neighbor.val, [])
#                     queue.append(neighbor)
                    
#                 clone_map[cur].neighbors.append(clone_map[neighbor])
        
#         return clone_map[node]
        
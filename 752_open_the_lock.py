class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = collections.deque([('0000', 0)])
        visited = {'0000'}
        
        '''
        03242022 BFS问题，标准模板。
        把第一个元素放进queue中，在while 循环里不断从queue里pop出来
        设好边界，即当找到答案则返回，在限制deadends中则继续
        然后搜被pop出来Node的8个邻居，即每个数字可以加减1，可以用helper()
        剪枝：如果邻居已经被访问过就算了，如果没有就enqueue，继续露蒲。
        '''
        
        while q:
            node, val = q.popleft()
            if node == target:
                return val
            if node in deadends:
                continue
            
            # put current node's all 8 neighbors into queue
            neighbors = self.helper(node)
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    # BFS: add one more depth
                    q.append((neighbor, val+1))
                    
        return -1
                    
            
    def helper(self, node):
        # return all 8 neighbors
        neighbors = []
        for i in range(4):
            cur_num = int(node[i])
            new_num1 = (cur_num + 1) % 10
            new_num2 = (cur_num - 1) % 10
            neighbors.append(node[:i] + str(new_num1) + node[i+1:])
            neighbors.append(node[:i] + str(new_num2) + node[i+1:])
            
        return neighbors
            
            
            
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # 如果相等，跳出题目，不然会走一圈
        if source == target:
            return 0
        
        '''
        先构建bus与stop的关系，即收集每个stop所有经过的bus, key = stop, value = [bus]
        反过来，每个bus会经过哪些stop 是题目routes来表示。像是双向邻接表
        
        用经典BFS模板，把初始站点放进去，开始找与它相通的next_stop 并加入queue中
        初始点为source, 即一个初始点。
        找到所有经过这个stop的所有bus 用bus_stop[stop]
        对于每一个bus， 如果访问过了则跳过，因为如果再上车，则没意义一直循环。
        如果没访问过，看这个bus还经过哪里，经过的所有stop则是所有下一站next_stop
        用routes[bus] 来获取next_stop list
        
        如果刚好找到答案了，则返回。
        如果没有，则把相关信息加入queue 进行下一层循环，跳车之后distance += 1
        
        特别情况，[[0, 1, 2, 3, 4, 5], [6, 7, 8]], source = 1, target = 4
        结果还是1，不用跳车，相当于直接从4上车。结果并不是1-2-3-4
        
        '''
        bus_stop = defaultdict(list)
        
        # 走一遍Input, 记录每个stop有哪些bus, 是dict里包含list
        for i, route in enumerate(routes):
            for stop in route:
                bus_stop[stop].append(i)
                
        visited_bus = set()
        visited_stop = {source, }  # set with init value
        start = {source, }  # 像是一个queue, 包含当前起点站, 查找所有bus经过的下一站
        distance = 1
        
        while start:
            new_start = set()
            for stop in start:
                for bus in bus_stop[stop]:
                    if bus not in visited_bus:
                        visited_bus.add(bus)
                        
                        for next_stop in routes[bus]:
                            if  next_stop == target:
                                return distance
                            else:
                                new_start.add(next_stop)
                                visited_stop.add(next_stop)
                                
            distance += 1
            start = new_start
            
        return -1
                                
                
                
        
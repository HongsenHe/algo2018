class Solution:
    def numSquares(self, n: int) -> int:
        q = [n]
        sq_sums = [i*i for i in range(int(math.sqrt(n))+1)]
        level = 0
        
        '''
        经典BFS 题，先构造一个矩阵为了找邻居，也就是sq_sums [1, 4, 9..]直到刚好小于n
        如何构造queue和邻居问题，还有设定返回值问题？
        参考2sum问题，queue可以是target - sq_sum，然后不断enqueue, dequeue
        enqueue什么？每次都遍历sq_sums作为enqueue的候选人
        边界条件有哪些？参考2sum, 也就是找到！或者当前的数值已经小于sq_sum 无法构造了
        
        '''
        
        while q:
            level += 1
            q1 = []
            for num in q:
                for sq_sum in sq_sums:
                    if sq_sum == num:
                        return level
                    elif num < sq_sum:
                        break
                    else:
                        q1.append(num - sq_sum)
            q = q1
                
        return level
            
            
        
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        cur_gas = 0
        start_idx = 0
        
        '''
        两个变量total_gas和cur_gas 分别累加表示从起点开始总的油和当前的油
        如果当前的油 < 0, 就是不能从这个点出发，也就需要另找起点，
        start_idx = i + 1， 同时reset 当前的油，cur_gas = 0
        如果走到末尾，总剩余油量 >= 0 说明可以走完整个加油站。并且返回起点值
        '''

        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            cur_gas += gas[i] - cost[i]
            
            if cur_gas < 0:
                start_idx = i + 1
                cur_gas = 0
        
        if total_gas >= 0:
            return start_idx
        
        return -1
        
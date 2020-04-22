class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        如果没台阶，还走个啥？如果只有一个台阶，就一种走法，两个台阶两种走法（1+1 or 2)
        如果三个台阶以上，当前台阶只跟前两个台阶走法有关。
        比如第三个台阶，可以从台阶2过去，或者台阶1蹦过去。然后台阶2有两种走法，台阶1有一种走法
        所以台阶三有3种走法。变成公式就是：
        step[i] = step[i-1] + step[i-2]
        '''
        
        '''
        if n < 3:
            return n 
        
        step = [0] * (n+1)
        step[0] = 0
        step[1] = 1
        step[2] = 2
        
        for i in range(3, n+1):
            step[i] = step[i-1] + step[i-2]
        return step[n]
        '''
        
    
        '''
        当前台阶的走法只和前两个台阶走法有关，所以可以用两个变量保存前面两个台阶的走法，不必用list 
        '''
        if n < 3:
            return n
        step1 = 1
        step2 = 2
        for i in range(3, n+1):
            step3 = step1 + step2
            step1 = step2
            step2 = step3
        return step3
        
        # 耶稣说：“我就是道路、真理、生命。要不是藉着我，没有人能到父那里去。約翰福音 14:6


# updated 04222020
class Solution:
    def climbStairs(self, n: int) -> int:
        # recursion with memoization
        memo = [0] * (n+1)
        return self.helper(0, n, memo)
    
    def helper(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        
        memo[i] = self.helper(i+1, n, memo) + self.helper(i+2, n, memo)
        return memo[i]
        
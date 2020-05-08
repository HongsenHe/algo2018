# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candi_cele = 0
        
        '''
        很有意思的现象
        如果i 知道j 那么i肯定不是celebrity,  因为真明星不知道任何人。。
            更新candi_cele = i
        如果i 不知道j 那j 也不是celebrity, 因为连i都不知道他。。。
            跳过for loop
            
        最后选出来的candi_cele 要再检查一遍
        如果候选人知道谁，或者某人不知道他，就是假明星， 不然就返回真明星。
        '''
        for i in range(1, n):
            if knows(candi_cele, i):
                candi_cele = i
        
        for j in range(n):
            if candi_cele == j:
                continue
            if knows(candi_cele, j) or not knows(j, candi_cele):
                return -1
            
        return candi_cele
        
            
                    
                    
            
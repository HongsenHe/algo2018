class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        '''
        很多edge cases
        1. 如果当前有花，则不种花
        2. 如果前面有花，也不能种花 （考虑‘有前面’即 i > 0）
        3. 如果后面有花，也不能种花。（考虑‘有后面’即 i < len(flowerbed) - 1)
        4. 其他情况 可以种花，答案加1，并且改变当前值，（会影响到后续种花条件）
        '''
        
        res = 0
        
        for i, value in enumerate(flowerbed):
            if value:
                continue
                
            if i > 0 and flowerbed[i - 1]:
                continue
                
            if i < len(flowerbed) - 1 and flowerbed[i + 1]:
                continue
                
            res += 1
            flowerbed[i] = 1
            
        return res >= n
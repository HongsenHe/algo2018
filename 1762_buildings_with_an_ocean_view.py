class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        sk = []
        res = []
        
        for i in range(len(heights)):
            height = heights[i]
            
            while sk and height >= heights[sk[-1]]:
                sk.pop()
                
            sk.append(i)
            
        return sk
                
            
            
        
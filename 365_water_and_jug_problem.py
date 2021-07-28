class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        
        '''
        ax + by = c = gcd(a, b), nc = z and z <= x+y
        '''
            
        return targetCapacity % self.gcd(jug1Capacity, jug2Capacity) == 0
        
    def gcd(self, jug1Capacity, jug2Capacity):
        if jug2Capacity == 0:
            return jug1Capacity
        return self.gcd(jug2Capacity, jug1Capacity % jug2Capacity)
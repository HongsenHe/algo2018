class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        # todo
        heaters.sort()
        res = 0
        
        for house in houses:
            radius = float('inf')
            left = bisect.bisect_right(heaters, house)
            if left > 0:
                radius = min(radius, house-heaters[left-1])

            right = bisect.bisect_left(heaters, house)
            if right < len(heaters):
                radius = min(radius, heaters[right]-house)
            
            res = max(res, radius)
        return res
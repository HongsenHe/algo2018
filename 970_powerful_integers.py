class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        for i in range(20):
            for j in range(20):
                cur = pow(x, i) + pow(y, j)
                if cur <= bound:
                    res.add(cur)
        return res
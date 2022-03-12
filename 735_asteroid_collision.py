class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        sk = []
        
        for aster in asteroids:
            # different direction, 必须当前的小行星<0, 向左，sk的top向右才能相撞
            while sk and aster < 0 < sk[-1]:
                cur_top = sk[-1]
                
                # 质量相等，都爆，弹出当前sk top退出
                if abs(cur_top) == abs(aster):
                    sk.pop()
                    break
                elif abs(cur_top) > abs(aster):
                    break
                else:
                    sk.pop()
            else: 
                # init or same direction
                sk.append(aster)
                
        return sk

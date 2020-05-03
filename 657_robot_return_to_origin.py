class Solution:
    def judgeCircle(self, moves: str) -> bool:
        up_down = 0
        left_right = 0
        
        for move in moves:
            if move == 'U':
                up_down += 1
            elif move == 'D':
                up_down -= 1
            elif move == 'L':
                left_right += 1
            elif move == 'R':
                left_right -= 1
    
        return up_down == 0 and left_right == 0
            
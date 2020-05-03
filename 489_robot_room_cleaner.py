# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # 先四个方向
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        '''
        大思路还是DFS 回溯，一直走，如果行就搜四个方向并且标记访问过，
        走完就回头，不行就右转，继续搜索。
        '''
        return self.dfs((0, 0), robot, 0, set())
        
    def go_back(self, robot):
        # 如何回溯退后？先转180度回头，走一步，再转180度就回到了前一个位置
        robot.turnLeft()
        robot.turnLeft()
        robot.move()
        robot.turnLeft()
        robot.turnLeft()
        
    def dfs(self, cell, robot, d, visited):
        # 如果当前的坐标已经访问过就不必继续了, 如果还没，就加入访问集合并且清理此地
        if cell in visited:
            return

        visited.add(cell)
        robot.clean()
        
        for _ in self.directions:
            if robot.move():
                '''
                如果当前可以走下去就一直走，
                在当前的cell更新一下成为下一个要去的地方，用d来控制方向
                每次走完都要回头（回溯）然后继续走
                '''
                new_cell = (cell[0] + self.directions[d][0],
                            cell[1] + self.directions[d][1])
                self.dfs(new_cell, robot, d, visited)
                self.go_back(robot)
                
            # 如果走不下去就用右手定则，每次走右边
            robot.turnRight()
            # 在大循环for directions下面，每一轮dfs都要改变d的值，因为每次递归都要走四个方向
            d = (d + 1) % 4
            
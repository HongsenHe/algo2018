
class BrowserHistory:

    def __init__(self, homepage: str):
        # 可以用stack的思想，但sk pop出去的数字就无法追踪了，除非用另一个stack记录。
        # 此题用list比较方便，因为可以用current position
        self.history = [homepage]
        self.cur_pos = 0
        

    def visit(self, url: str) -> None:
        # 对于一个新的url, 要从此开始，即把当前位置cur_pos之后的都弹出去
        while self.history and len(self.history) - 1 > self.cur_pos:
            self.history.pop()
            
        self.history.append(url)
        self.cur_pos += 1
        

    def back(self, steps: int) -> str:
        # 当前的指针减去steps即可，但不能越界。比如cur_pos = 3, steps = 4
        # 只能后退三步，即 3 - 3 = 0 退到0 即答案
        max_back = min(steps, self.cur_pos)
        self.cur_pos -= max_back
        return self.history[self.cur_pos]

    
    def forward(self, steps: int) -> str:
        # 当前指针加上steps, 但不能越界len(history) - 1, 比如cur_pos = 3
        # step = 4, 总长度是6, (idx = 5), cur_pos = min(5, 3+4)
        self.cur_pos += steps
        self.cur_pos = min(self.cur_pos, len(self.history) - 1)
        
        return self.history[self.cur_pos]
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
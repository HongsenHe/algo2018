class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return None
        
        while not self.empty():
            self.q2.append(self.q1.pop(0))
        
        pop_node = self.q2.pop()
        for i in range(len(self.q2)):
            self.q1.append(self.q2.pop(0))
        return pop_node
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return None
        
        while not self.empty():
            self.q2.append(self.q1.pop(0))
        
        top_node = self.q2[-1]
        for i in range(len(self.q2)):
            self.q1.append(self.q2.pop(0))
        return top_node
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
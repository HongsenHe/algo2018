class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sk1 = []
        self.sk2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.sk1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return None
        for i in range(len(self.sk1)):
            self.sk2.append(self.sk1.pop())
        pop_node = self.sk2.pop()
        
        for i in range(len(self.sk2)):
            self.sk1.append(self.sk2.pop())
        return pop_node
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return None
        for i in range(len(self.sk1)):
            self.sk2.append(self.sk1.pop())
        peek_node = self.sk2[-1]
        for i in range(len(self.sk2)):
            self.sk1.append(self.sk2.pop())
        return peek_node
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.sk1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
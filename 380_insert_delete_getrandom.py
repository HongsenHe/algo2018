class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.val2idx = {}
        

    def insert(self, val: int) -> bool:
        if val in self.val2idx:
            return False
    
        self.nums.append(val)
        self.val2idx[val] = len(self.nums) - 1
        
        return True
    

    def remove(self, val: int) -> bool:
        if val not in self.val2idx:
            return False
        
        '''
        1. 把当前val的index找出来
        2. 用nums最后一个元素来覆盖这个index的位置
        3. 更新 dict
        4. 删除最后一个元素
        5. 从dict里也删除
    
        '''
        idx = self.val2idx[val]
        last = self.nums[-1]
        
        self.nums[idx] = last
        self.val2idx[last] = idx

        self.nums.pop()
        del self.val2idx[val]
        
        return True
        

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
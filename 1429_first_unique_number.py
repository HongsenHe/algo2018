class FirstUnique:

    def __init__(self, nums: List[int]):
        '''
        03092022
        要保持unique，则需要一个set, 或者hashmap, kv来维持。
        因为不断加新数字，则用hashmap比较方便。
        set无法记录历史，除非新数字已经在set里了，然后删
        
        保持first，则用一个queue来表达，把非unique pop出来后
        第一个数字就是first and unique了
        
        showFirstUnique的操作并不是O(N), 而是O(1) 因为pop()
        因为只删掉一次，非unique的数字，之后就人容易操作了。
        让当前数字变成非unique的方法就是调用add(), 即加入了重复数字。
        
        空间用了O(N)
        
        '''
        self.cache = Counter(nums)
        self.uniques = nums

    def showFirstUnique(self) -> int:
        while self.uniques and self.cache[self.uniques[0]] > 1:
            self.uniques.pop(0)
            
        if self.uniques:
            return self.uniques[0]
        else:
            return -1
        

    def add(self, value: int) -> None:
        self.uniques.append(value)
        self.cache[value] += 1
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
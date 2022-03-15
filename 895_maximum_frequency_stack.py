import heapq

class FreqStack:
    '''
    用一个dict 来表示每个字母的个数 
    用另一个dict(list)来表示，Key = count, value 是拥有这些个数字母的列表
    这样在插入的时候，有了append的顺序，则返回最后的。(stack top)
    比如 个数= 2， 字母列表是[abab] （按插入顺序排序stack FILO, 则返回b
    
    pop() 每次都返回freq_group里most_freq的那一列字母的 最后一个
    如果都弹出去了，则most_freq -= 1. 直到继续push进来，更新most_freq
    
    '''
    

    def __init__(self):
        self.freq = {}
        self.freq_group = defaultdict(list)
        self.max_freq = 0
        
    def push(self, val: int) -> None:
        new_freq = self.freq.get(val, 0) + 1
        self.freq[val] = new_freq
        
        self.max_freq = max(self.max_freq, new_freq)
        self.freq_group[new_freq].append(val)

    def pop(self) -> int:
        elem = self.freq_group[self.max_freq].pop()
        self.freq[elem] -= 1
        
        if not self.freq_group[self.max_freq]:
            self.max_freq -= 1
            
        return elem
        
        
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
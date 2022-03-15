class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        res = ['$']
        
        '''
        每次都从最多元素的一组拿字符串，比如'aab'，拿'a'
        如果'a'刚好不是res里 最后的一个（即相邻两个元素不一样）
        则加入res list, 并且a的cnt -= 1, 如果是空的则删除'a'
        完成后，则无需看'a'了，否则和res重复，即break
        
        此时counter = 'ab', a和b都是最多元素的组合。
        则都试试！因此使用for loop to most_common set
        
        此处设置一个stopper， 来判断是否要推出while loop.
        
        '''
        
        while counter:
            stop = True
            for value, count in counter.most_common():
                if value != res[-1]:
                    res.append(value)
                    counter[value] -= 1
                    
                    if counter[value] == 0:
                        del counter[value]
                        
                    stop = False
                        
                    # 只从当前最多元素的集合中(most_common)选择一个加入res里
                    # 所以可以break 此处循环。
                    break
                    
            if stop: break
                    
        if len(res) == len(s) + 1:
            return ''.join(res[1:])
        
        return ""
        
            
                
                
        
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        
        '''
        用一个next变量来表示当前iterator的下一个变量
        如果调用peek() 则直接返回此next (peak)
        
        如果调用next() 则需要更新当前指针，并且返回next
        因为next已经表示了下一个
        
        更新当前指针：如果下一个还有，则更新next
        如果没了，就是None
        
        hasNext(), 如果iter还有，或者next变量还有
        相当于提前拿出来下一个元素，放到next里
        
        '''
        self.iter = iterator
        self.next1 = iterator.next()

        
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.next1

    def next(self):
        """
        :rtype: int
        """
        res = self.next1
        if self.iter.hasNext():
            self.next1 = self.iter.next()
        else:
            self.next1 = None
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.iter.hasNext() or self.next1 is not None
# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].



'''
what if you only have next() function, but no hasNext() function?

# it = [1, 2, 3].__iter__()
# next(it) -> 1, 2, 3, throw ERROR

# PeekingIterator(it):
#   next() -> next element, 
#   has_next() -> does next element exist?
#   peek() -> next element without consuming the iterator


class PeekingIterator(object):
    def __init__(self, it):
        self.top = 0
        self.top_status = False
        self.it = it
        
    def next(self):
        if self.has_next():
            res = self.top
            # reset
            self.top_status = False
            self.top = 0
            return res
        else:
            return None
    
    def has_next(self):
        try:
            if self.top_status:
                return True
            else:
                self.top = next(self.it)
                self.top_status = True
                return True
        except StopIteration:
            self.top_status = False
            return False
            
    def peek(self):
        if self.top_status:
            return self.top
        
        if self.has_next():
            return self.top

        return None

    
it = iter([1, 2, 3])
obj = PeekingIterator(it)
print(obj.next()) # 1
print(obj.peek()) # 1
print(obj.next()) # 2
print(obj.next()) # 3
print(obj.has_next()) # False 

'''
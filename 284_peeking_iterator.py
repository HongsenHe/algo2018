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
'''
搞个大cache！如果Peek就是返回大缓存，如果next就是更新这个缓存啦！
'''
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.cache = iterator.next()

        
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.cache

    def next(self):
        """
        :rtype: int
        """
        res = self.cache
        if self.iter.hasNext():
            self.cache = self.iter.next()
        else:
            self.cache = None
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.iter.hasNext() or self.cache is not None
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
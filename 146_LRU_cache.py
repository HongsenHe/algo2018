'''
hashmap to save key/value pair
double linked list to save each node
everytime call get/put function, call renew:
    1. remove entry (node) from current double list
    2. insert this entry to the tail
if > capacity, remove the head node

LRU: the head node is the least recent used node!
'''


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.dummyNode = Node(-1, -1)
        self.tail = self.dummyNode
        self.entryFinder = {}
        

    def get(self, key: int) -> int:
        entry = self.entryFinder.get(key)
        if entry is None:
            return -1
        else:
            self.renew(entry)
            return entry.val
        

    def put(self, key: int, value: int) -> None:
        entry = self.entryFinder.get(key)
        if entry is None:
            # setup dic with key and entry(k,v)
            entry = Node(key, value)
            self.entryFinder[key] = entry
            
            # update tail with new node
            self.tail.next = entry
            entry.prev = self.tail
            self.tail = entry
            
            if self.size < self.capacity:
                self.size += 1
            else:
                # double link dummy and head.next, thus del head
                headNode = self.dummyNode.next
                if headNode is not None:
                    self.dummyNode.next = headNode.next
                    headNode.next.prev = self.dummyNode
                # also del head (the least used node) form dic
                del self.entryFinder[headNode.key]
        else:
            entry.val = value
            self.renew(entry)
            
    def renew(self, entry):
        if self.tail != entry:
            # tmp delete entry from current position, then insert to the tail
            prevNode = entry.prev
            nextNode = entry.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            entry.next = None
            
            # insert new node to the tail
            self.tail.next = entry
            entry.prev = self.tail
            self.tail = entry
                
            

# another way
import collections
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    # @return an integer
    def get(self, key):
        if not key in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
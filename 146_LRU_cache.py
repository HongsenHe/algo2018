class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
        
class LRUCache:
    '''
    基本上是HashMap + doubled LinkedList思想。
    HashMap里key是数字，value是实际node用于创建链表。
    
    调用get方法: 如果在hashmap里直接返回，并且更新链表。因为已经被调用了
    所以要更新‘最后使用时间’即LRU的意义。 
    更新链表的算法是把这个节点放到最后（因为刚刚被使用）
    即调用renew() 
    
    调用put方法: 如果key不在hashmap里，要创建一个新节点。
    放到hashmap里，并且放到链表最后。如果目前hashmap已经超过容量了，
    则删掉head，因为这是最旧的数据。即调用 delete_head()
    如果key已经在hashmap里，则更新链表。
    
    '''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.finder = {}
        self.dummy = Node()
        self.tail = self.dummy
        

    def get(self, key: int) -> int:
        node = self.finder.get(key, None)
        
        if not node:
            return -1
        else:
            self.renew(node)
            return node.val
            

    def put(self, key: int, value: int) -> None:
        node = self.finder.get(key, None)
        
        if not node:
            # create a new node based on current key and value and insert into finder
            new_node = Node(key, value)
            self.finder[key] = new_node
            
            # insert new node to the tail
            self.append_node(new_node)

            # delete head if > LRU capacity
            if len(self.finder) > self.capacity:
                self.delete_head()
        else:
            # LRU algorithm
            node.val = value
            self.renew(node)
                    
                
    def renew(self, node):
        # change prev -> node -> next ... -> tail
        # to prev -> next ... -> tail -> node
        if self.tail != node:
            # delete the node from current position
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            node.next = None
            
            # insert new node to the tail
            self.append_node(node)
            
    def append_node(self, node):
        # change prev -> tail to prev -> node (tail)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

        
    def delete_head(self):
        # change dummy -> head -> next to dummy -> next
        head = self.dummy.next
        self.dummy.next = head.next
        head.next.prev = self.dummy

        del self.finder[head.key]
        
        
        
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        mp = {}
        
        # step 1: put all nodes into the pool only, no connection
        # key is original node, value is the clone val
        dummy = head
        while dummy:
            mp[dummy] = Node(dummy.val)
            dummy = dummy.next
            
        # step 2: reset, copy next and random pointer
        dummy = head
        while dummy:
            '''
            eg: 1 -> 2 -> 3 -> 4
            dummy is 1, mp[dummy] 1' is the clone one
            mp[dummy].next should be 2'
            dummy.next = 2, then mp[dummy.next] is 2'
            same as random pointer
            already copied node.val
            '''
            if dummy.next:
                mp[dummy].next = mp[dummy.next]
            if dummy.random:
                mp[dummy].random = mp[dummy.random]
            
            dummy = dummy.next
            
        # should return 1' clone's head, which is mp[original head]
        return mp[head]

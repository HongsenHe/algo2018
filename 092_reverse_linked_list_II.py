# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        go = dummy
        prev = None
        
        # keep going until find start point m, m is not the idx, so use m-1
        for _ in range(m-1):
            go = go.next
            
        # reverse from start node, but remember this node by start_fix
        start = start_fix = go.next
            
        # reverse how many nodes? 
        for _ in range(n-m+1):
            # reverse template
            tmp = start.next
            start.next = prev
            prev = start
            start = tmp
        
        # connect reversed part with the entire link list
        go.next = prev
        start_fix.next = start
        
        return dummy.next
        
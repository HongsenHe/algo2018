# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        inter_node = self.find_intersection(head)
        if not inter_node:
            return None

        p1 = head
        p2 = inter_node
        
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
            
        return p1
            
                
    def find_intersection(self, head):
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return slow
        
        return None

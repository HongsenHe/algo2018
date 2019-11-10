# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev = ListNode(0)
        prev.next = head
        slow = prev
        fast = prev
        for i in range(n+1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        return prev.next
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        node = head
        while node and count < k:
            node = node.next
            count += 1
        if count < k:
            return head
        
        new_head, prev = self.swap(head, count)
        head.next = self.reverseKGroup(new_head, k)
        return prev
    
    def swap(self, head, k):
        dummy = None
        while k > 0:
            tmp = head.next
            head.next = dummy
            dummy = head
            head = tmp
            k -= 1
        return (head, dummy)

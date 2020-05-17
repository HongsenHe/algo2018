# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        odd = head
        even = head.next
        even_head = even
        
        while even and even.next:
            '''
            1 -> 2 -> 3 -> 4
            1 is odd/head, 2 is even/even_head
            
            1 should link to 3, and 1 jump to 3
            then 1.next = 2.next, odd.next = even.next, odd = odd.next
            2 should link to 4, and 2 jump to 4
            then 2.next = 3.next, even.next = odd.next, even = even.next
            '''
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            
        # link 1 -> 3 to 2 -> 4, even_head is a fixed node
        odd.next = even_head
                
        return head
            
        
        
        
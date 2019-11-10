# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        mid = self.find_mid(head)
        right_list = self.sortList(mid.next) 
        mid.next = None
        left_list = self.sortList(head)
        
        return self.merge(left_list, right_list)
    
    def merge(self, left, right):
        dummy = ListNode(0)
        cur = dummy
        
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
                
            cur = cur.next
                
        if left:
            cur.next = left
        if right:
            cur.next = right
            
        return dummy.next
        
        
        
    def find_mid(self, head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
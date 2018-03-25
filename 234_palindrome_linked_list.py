# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        '''
        a very typical question: 
        #1 find linked list middle point
        #2 reverse a linked list
        #3 panlindrome concetp
        '''
        
        if not head:
            return True
        
        mid = self.findMid(head)
        tail = self.reverseList(mid.next)
        while tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True
        
    def findMid(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
            
    def reverseList(self, head):
        dummy = None
        while head:
            tmp = head.next
            head.next = dummy
            dummy = head
            head = tmp
        return dummy
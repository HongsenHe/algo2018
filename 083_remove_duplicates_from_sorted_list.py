# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        # create a dummy node, this is a fixed node
        # keep moving head, and return this dummy
        dummy = head
        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return dummy

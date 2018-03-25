# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # get len diff, then move the longer one first, until same len
        # and go together, if current node are the same, ok!
        lenA = self.getListLen(headA)
        lenB = self.getListLen(headB)
        diff = abs(lenA-lenB)
        
        if lenA > lenB:
            # move list A first
            headA = self.moveList(headA, diff)
        else:
            headB = self.moveList(headB, diff)
            
        # now they have same length and compare current node
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
            
    def moveList(self, head, step):
        for i in range(step):
            head = head.next
        return head
        
    def getListLen(self, head):
        length = 0
        if not head:
            return 0
        
        while head:
            length += 1
            head = head.next
        return length
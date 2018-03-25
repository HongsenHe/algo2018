# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        dummy = head # this dummy node will keep moving
        carry = 0
        
        # either l1 or l2 has value, or carry exits
        while l1 or l2 or carry:
            subSum = carry # add previous digit carry 0/1
            carry = 0 # reset this round carry
            
            if l1:
                subSum += l1.val
                l1 = l1.next
            if l2:
                subSum += l2.val
                l2 = l2.next
            if subSum > 9:
                # eg. this round result subSum = 13, then only store 3
                # and set carry to 1 then pass to next round
                carry = 1
                subSum -= 10
                
            dummy.next = ListNode(subSum)
            dummy = dummy.next
            
        return head.next
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        '''
        input node is the node you want to delete, how to skip this node?
        1->2->3->4, then just set input node value as next node value, and change pointer
        '''
        node.val = node.next.val # now this position value is 4, not 3
        node.next = node.next.next # now this node with 4 will link to original node4 next...
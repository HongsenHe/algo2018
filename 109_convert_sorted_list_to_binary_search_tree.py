# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        
        mid = self.find_mid(head)
        node = TreeNode(mid.val)
        
        if head == mid:
            return node
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        
        return node
    
    def find_mid(self, head):
        # help to disconnect the left half from the mid node
        dummy = None
        slow = fast = head
        while fast and fast.next:
            dummy = slow
            slow = slow.next
            fast = fast.next.next
        if dummy:
            dummy.next = None
        return slow
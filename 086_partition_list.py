# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        '''
        quicksort 并不是一个好思路，因为还要保持顺序。
        可以创建两个dummy node, 来代表所有小于x的list 和 大于x的list
        然后走一遍原List，最后再合并这两个list 因为是linkedlist
        所以没有额外空间，只是改变指针方向，Time O(n)
        '''
        
        small_node = small_head = ListNode(0)
        big_node = big_head = ListNode(0)
        
        while head:
            if head.val < x:
                small_node.next = head
                small_node = small_node.next
            else:
                big_node.next = head
                big_node = big_node.next
                
            head = head.next
            
        big_node.next = None
        small_node.next = big_head.next
        
        return small_head.next
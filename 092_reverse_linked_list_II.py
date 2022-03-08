# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        b4_rev_head = dummy
        
        '''
        03082022
        保留一个基准 (dummy) 返回基准的后面即是答案： dummy.next
        先找到翻转之前的node, 即 b4_rev_head (1)
        经典翻转算法，要记得最后一个元素(4) 将来和 (1) 连接
        即 b4_rev_head.next = prev    1 -> (4-3-2)
        再把2和5连接，即需要一个node来记得翻转之前2的位置。
        即 rev_head_fix(2).next = rev_head(5)
        
        
        '''
        
        # dummy - 1 - (2 - 3 - 4) - 5, b4_rev_head should be 1
        for i in range(left - 1):
            b4_rev_head = b4_rev_head.next
            
        rev_head = rev_head_fix = b4_rev_head.next
        
        # reverse template
        prev = None
        for _ in range(right - left + 1):
            tmp = rev_head.next
            rev_head.next = prev
            prev = rev_head
            rev_head = tmp
            
        b4_rev_head.next = prev
        rev_head_fix.next = rev_head
        
        # 所有折腾排序都在一个基准(dummy)的后面(next)完成，最后返回dummy.next即可
        return dummy.next
   
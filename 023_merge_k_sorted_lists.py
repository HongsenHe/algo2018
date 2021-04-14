# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

# 重写，来比较node.val 记一下。
ListNode.__lt__ = lambda x, y: (x.val < y.val)

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        # 常规写法，一个不断跑dummy, 一个固定点最后返回dummy_head.next
        dummy = dummy_head = ListNode(0)
        heap = []
        # 循环一次input, 对于每一个list把他们都放进堆中，
        # 自然就以node.val排序了。
        for head in lists:
            if head:
                heapq.heappush(heap, head)
                
        while heap:
            # 弹出来的就是最小的，python默认min heap
            head = heapq.heappop(heap)
            
            # 赋值
            dummy.next = head
            dummy = dummy.next
            
            # 如果当前list还有元素则继续加入Heap,  然后重排序
            if head.next:
                heapq.heappush(heap, head.next)
                    
        return dummy_head.next
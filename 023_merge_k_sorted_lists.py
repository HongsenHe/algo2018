# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        
        head = dummy = ListNode(0)
        q = PriorityQueue()
        
        # 把每个list的首个node放进去，已经排序过
        for l in lists:
            if l:
                q.put(Wrapper(l))
                
        while not q.empty():
            node = q.get().node
            dummy.next = node
            dummy = dummy.next
            node = node.next
            # 当前node是最小值，放到结果里，如果还有下一个，继续放入q
            if node:
                q.put(Wrapper(node))
                
        return head.next
        
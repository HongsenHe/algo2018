# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # 如果t1 t2不是空的，那就用他们的数值附上新的节点，然后分别计算左边和右边
        # 每一次左边节点可以当做一个新的节点root，不然就返回t1 or t2不是空的
        if t1 and t2:
            t3 = TreeNode(t1.val + t2.val)
            t3.left = self.mergeTrees(t1.left, t2.left)
            t3.right = self.mergeTrees(t1.right, t2.right)
            return t3
        else:
            return t1 or t2
        
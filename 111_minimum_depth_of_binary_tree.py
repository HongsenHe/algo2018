# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 如果没有左子树或者右子树，不能取左右子树最小的，因为是0
        if not root:
            return 0
        if not root.left:
            # 如果没有左子树，就转而求右子树最小值，加上父节点
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left),
                   self.minDepth(root.right)) + 1
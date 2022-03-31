# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # BST 的中序遍历的特制：有序啊！
        sk = []
        while root or sk:
            if root:
                sk.append(root)
                root = root.left
            else:
                cur = sk.pop()
                k -= 1
                if k == 0:
                    return cur.val
                root = cur.right
            
        return -1
        
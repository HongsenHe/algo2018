# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
#         sk = []
#         res = []
        
#         '''
#         基本套路用stack, 中序遍历是左root右。就先写个while 一直跑 left tree
#         放到 stack里。如果放满了就开始pop stack. pop出来的就是root
#         即放到res list里。此时转向当前节点的right tree，即root = cur.right
        
#         '''
        
#         while root or sk:
#             while root:
#                 sk.append(root)
#                 root = root.left
        
#             cur = sk.pop()
#             res.append(cur.val)
#             root = cur.right
            
#         return res

        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if not root:
            return
        
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)
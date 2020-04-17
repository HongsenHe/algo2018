# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        
        '''
        postorder 每次调用pop()就是root节点，
        在inorder，左侧[:idx]就是这个root的左子树，[idx+1:]就是右子树
        postorder是左右根，所以build是要从根右左的顺序
        每次调用buildTree, 都返回当前的root, 里面包含他的子树。
        '''
        root = TreeNode(postorder.pop())
        idx = inorder.index(root.val)
        root.right = self.buildTree(inorder[idx+1:], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)
        
        return root
        
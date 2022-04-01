# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        
        '''
        找中旬遍历时候的下一个节点。
        如果p 比root大，则可以忽略左子树，答案可能在root的右子树（或没有）
        如果p 比root小，则当前root可能是个答案，同时移动到左子树。
        
        '''
        
        while root:
            
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
                
        return successor
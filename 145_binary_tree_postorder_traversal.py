# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorder(self, root):
        res = []
        if not root:
            return res
        
        sk = [root]
            
        # 05152021
        '''
        postorder顺序是 left right root. 最后加入root节点
        也可以说把root节点放到res list的前面。
        每次弹出来一个节点即root, 压入stack里。如果有left tree
        压入stack， 同理right tree
        
        此题不能先一天路走到黑，去让root = root.left， 因为即使
        left tree到底了，还需要有right tree. 都有了才能 插入
        他们的root. 
        既然顺序是从上到下，不妨每次访问root的时候就插入res list
        用反序的方式。
        '''

        while sk:
            root = sk.pop()
            res.insert(0, root.val)
            if root.left:
                sk.append(root.left)
            if root.right:
                sk.append(root.right)
            
        return res
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(res, root)
        return res
        
    def helper(self, res, root):
        if not root:
            return
        
        self.helper(res, root.left)
        self.helper(res, root.right)     
        res.append(root.val)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        
        '''
        用一个dfs子函数来计算，对于当前的root节点，如果不存在，则返回None
        递归通用：root.left = dfs(root.left, xxx)
        
        如果当前的root节点刚好在删除列表里，则
        如果还有 child, 则加入到res list. 并且让root 为空
        因为是DFS的方法，所以先加[6][7]
        
        '''
        
        def dfs(root, res):
            if not root:
                return None

            root.left = dfs(root.left, res)
            root.right = dfs(root.right, res)

            if root.val in to_delete:
                if root.left:
                    res.append(root.left)
                if root.right:
                    res.append(root.right)

                root = None
            
            return root
                    
        if dfs(root, res):
            res.append(root)
            
        return res
                
            
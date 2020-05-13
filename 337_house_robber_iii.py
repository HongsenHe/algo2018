# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        # 方法1： 
        # if not root:
        #     return 0
        # val = root.val
        
        '''
        这两种情况选最大方案。
        1. 抢root,就不能抢root的孩子left, right, 
            只能抢孙子left.left, left.right, right.left and right.right
        2. 不抢root, 就可以抢root的孩子root.left + root.right
        
        可以优化，记录被抢过节点的数字
        比如计算root.left.left的时候，其实已经从root.left中得到答案。
        '''
        
#         if root.left:
#             val += self.rob(root.left.left) + self.rob(root.left.right)
#         if root.right:
#             val += self.rob(root.right.left) + self.rob(root.right.right)
            
#         return max(val, self.rob(root.left) + self.rob(root.right))


        # 方法2
        mem = {}
        return self.helper(root, mem)
    
    def helper(self, root, mem):
        if not root:
            return 0
        # 区别就在这里，用mem来记录所有访问过节点的解。
        if root in mem:
            return mem[root]
        
        val = root.val
        if root.left:
            val += self.helper(root.left.left, mem) + self.helper(root.left.right, mem)
        if root.right:
            val += self.helper(root.right.left, mem) + self.helper(root.right.right, mem)
            
        val = max(val, self.helper(root.left, mem) + self.helper(root.right, mem))
        # 把当前root的最终最优解放进去，并且返回当前root的解，层层递归
        mem[root] = val
        
        return val

            
        
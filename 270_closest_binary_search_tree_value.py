# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        diff = float('inf')
        res = 0

        '''
        如果target比当前root小，则root = root.left
        因为如果去右子树，则距离比左子树更大，但也可能root距离target更近
        所以也需要一个全局变量打擂台。
        
        '''

        while root:
            if abs(target-root.val) < diff:
                diff = abs(target-root.val)
                res = root.val
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return res
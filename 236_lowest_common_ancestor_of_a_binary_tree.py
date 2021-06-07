# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        '''
        如果根节点是空或者是等于p, q其中一个，那就返回根节点啦！
        如果p和q在root两边，那他们的根节点就是结果啦！
        即某个节点的左右子树分别包含这两个节点，这节点就是答案啦！
        否则返回相应的左或者右子树，看看哪个包含p或者q的就返回哪个啦！
            2
           / \
          1   3
          
        root = 2, p = 1, q = 3
        left == p, right == 3, then return root = 2
        '''
        # 当前节点刚好碰到了所给的p或者q节点，那就返回吧，或者空。。。
        if not root or root == p or root == q:
            return root
        
        # divide 分别看左右子树，看看能否找到，在满足上述条件就跳出来
        # 如何理解：p和q 不变，就是已知条件，但如果现在的根节点不是root, 
        # 而是root.left 算法是一样的，（root.left也可能是答案LCA）
        # 分治法，把root.left 也看成根节点，然后计算。
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        '''
        conquer 现在有了当前节点的左右子树节点，如果都有东西，说明碰到了！
        p或者q 节点，那这个当前的root就是答案啦！一直返回上去

        如果只有一边有也没关系，就返回那个子树。
        但这个子树并不是最终答案，只是当前root的答案。
        '''
        if left and right:
            return root
        return left if left else right
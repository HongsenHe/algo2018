# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        return self.helper(root, arr, 0)
        
    
    def helper(self, root, arr, pos):
        # 这几种情况是错的：如果当前位置pos 越过了arr长度， 或者节点root 是空，或者当前节点数值根本不等
        if not root or pos == len(arr) or root.val != arr[pos]:
            return False
        
        # 这种情况是对的：当前位置pos到达了最后一个，并且这个节点没有左右子树，即叶子，并且当前节点 和当前arr数字相等
        if pos == len(arr) - 1 and not root.left and not root.right and root.val == arr[pos]:
            return True
        
        # 继续查找下一个节点，并且分别左右子树查找。用or表示只要有一个解即可。
        return self.helper(root.left, arr, pos+1) or self.helper(root.right, arr, pos+1)
        
        
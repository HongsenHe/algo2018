# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def postorder(root):
                return postorder(root.left) + postorder(root.right) + [root.val] if root else []
        return ' '.join(map(str, postorder(root)))

    
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def helper(lower, upper):
            if not data or data[-1] < lower or data[-1] > upper:
                return None
            cur = data.pop()
            root = TreeNode(cur)
            root.right = helper(cur, upper)
            root.left = helper(lower, cur)
            return root
        data = [int(x) for x in data.split(' ') if x]

        return helper(float('-inf'), float('inf'))
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
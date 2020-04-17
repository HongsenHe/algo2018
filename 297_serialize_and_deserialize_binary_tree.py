# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(root):
            if not root:
                res.append('#')
            else:
                res.append(str(root.val))
                helper(root.left)
                helper(root.right)
            
        res = []
        helper(root)
        return " ".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper():
            cur = next(data)
            if cur == '#':
                return None
            root = TreeNode(int(cur))
            root.left = helper()
            root.right = helper()
            return root
        data = iter(data.split(" "))

        return helper()
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
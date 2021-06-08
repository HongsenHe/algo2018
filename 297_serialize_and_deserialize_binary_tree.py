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
        
        '''
        把树的结构变成链表结构
        对于当前root, 如果是空，则放入特殊符号# 
        否则把root.val放入结果集中，同时操作左右子树
        最后把list变成str返回
        
        '''
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
        
        '''
        把链表结构变成树结构。
        首先把input从str变成list
        再弹出第一个数字，作为最顶的root
        如果弹出的是特殊字符#， 则略过。
        同时建立新的节点，赋值elem给root.
        同样对当前Root的左右子树操作，返回当前层的root
        
        '''
        def helper():
            elem = data.pop(0)
            if elem == '#':
                return None
            root = TreeNode(int(elem))
            root.left = helper()
            root.right = helper()
            return root
            
        data = data.split(" ")
        return helper()
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
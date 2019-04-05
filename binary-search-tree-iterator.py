# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
            
        

    def next(self):
        node = self.stack.pop()
        r = node.right
        while r:
            self.stack.append(r)
            r = r.left
        return node.val
            
        

    def hasNext(self):
        return len(self.stack)!=0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
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

"""
Time: init() O(1). next() O(LogN). hasNext() O(1).
Space: O(N)
"""   
class BSTIterator(object):

    def __init__(self, root):
        self.node = root
        self.stack = []
            
    def next(self):
        while self.node:
            self.stack.append(self.node)
            self.node = self.node.left
            
        node = self.stack.pop()
        self.node = node.right
        return node.val
        
    def hasNext(self):
        return self.stack or self.node


"""
FYI. Template for in-order traverse.
"""
def inOrderTraverse(root):
    stack = []
    node = root
    
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        
        node = stack.pop()
        
        #do something
        print node.val
        
        node = node.right
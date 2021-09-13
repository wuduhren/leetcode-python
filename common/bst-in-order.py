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
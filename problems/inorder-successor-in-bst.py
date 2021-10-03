"""
Time: O(N)
Space: O(N)

First, check if the p has right child, if it has a right child, we can continue the inorder traversal from it.
Second, if p does not have right child, we need to do the inorder traversal from the beginning.
During the traversal, do check if the prev is p.
If so, return the current node.
"""
class Solution(object):
    def inorderSuccessor(self, root, p):
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        else:
            stack = []
            node = root
            prev = None
            while node or stack:
                while node:
                    stack.append(node)
                    node = node.left
                
                node = stack.pop()
                
                if prev==p: return node

                prev = node
                node = node.right
            return None


"""
Inorder Traversal Template.
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
"""
Time: O(N)
Space: O(N)

Pre-Order Traversal
"""
class Solution(object):
    def flatten(self, root):
        if not root: return None
        
        preHead = TreeNode(0)
        curr = preHead
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
            
            node.right = None
            node.left = None
            curr.right = node
            curr = curr.right
            
        return preHead.right

"""
Time: O(N)
Space: O(1)

Morris Traversal
"""
class Solution(object):
    def flatten(self, root):
        node = root
        
        while node:
            if node.left:
                rightmost = node.left
                while rightmost.right: rightmost = rightmost.right
                rightmost.right = node.right
                node.right = node.left
                node.left = None
            else:
                node = node.right
        return root
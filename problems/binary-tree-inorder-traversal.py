"""
In-order traversal means that: if there is a left node, visit it first; visit the current node; then if there is right node, visit it.
In-order: Left->Current->Right
Pre-order: Current->Left->Right
Post-order: Left->Right->Current
"""
class Solution(object):
    def inorderTraversal(self, root):
        def helper(node):
            if not node: return
            helper(node.left)
            opt.append(node.val)
            helper(node.right)
            
        opt = []
        helper(root)
        return opt
        
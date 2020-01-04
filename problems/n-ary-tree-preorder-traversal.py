"""
Pre-order traversal means that: visit the current node; if there is a left node, visit it; then if there is right node, visit it.
In-order: Left->Current->Right
Pre-order: Current->Left->Right
Post-order: Left->Right->Current
"""
class Solution(object):
    def preorder(self, root):
        def helper(node):
            if not node: return
            opt.append(node.val)
            for child in node.children:
                helper(child)
        opt = []
        helper(root)
        return opt
"""
Post-order traversal means that: if there is a left node, visit it; then if there is right node, visit it; visit the current node.
In-order: Left->Current->Right
Pre-order: Current->Left->Right
Post-order: Left->Right->Current
"""
class Solution(object):
    def postorder(self, root):
        def helper(node):
            if not node: return
            for child in node.children:
                helper(child)
            opt.append(node.val)
        opt = []
        helper(root)
        return opt
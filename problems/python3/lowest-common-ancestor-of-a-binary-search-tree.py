"""
Recursive
Time: O(LogN) if the tree is balanced.
Space: O(LogN) for the recursion stack.
"""
class Solution:
    def lowestCommonAncestor(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if q.val<=node.val<=p.val or p.val<=node.val<=q.val:
            return node
        elif q.val<node.val and p.val<node.val:
            return self.lowestCommonAncestor(node.left, p, q)
        elif node.val<q.val and node.val<p.val:
            return self.lowestCommonAncestor(node.right, p, q)


"""
Iterative
Time: O(LogN) if the tree is balanced.
Space: O(1).
"""
class Solution:
    def lowestCommonAncestor(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while not (q.val<=node.val<=p.val or p.val<=node.val<=q.val):
            if q.val<node.val and p.val<node.val:
                node = node.left
            elif node.val<q.val and node.val<p.val:
                node = node.right
        return node
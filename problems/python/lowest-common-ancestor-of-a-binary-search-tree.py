"""
Time: O(LogN). O(N) if the tree is unbalanced.
Space: O(1)

If both p and q are both on the left subtree, then search the left subtree.
If both p and q are both on the right subtree, then search the right subtree.
Else the current must be the ans.
"""
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        node = root
        
        while node:
            if node.val>q.val and node.val>p.val:
                node = node.left
            elif node.val<q.val and node.val<p.val:
                node = node.right
            else:
                return node
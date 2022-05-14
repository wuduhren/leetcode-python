"""
Time: O(N)
Space: O(LogN) if the tree is balanced.
"""
class Solution:
    def isSameTree(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if not node1 and not node2:
            return True

        if (not node1 and node2) or (node1 and not node2):
            return False

        if node1.val!=node2.val:
            return False

        return self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right, node2.right)
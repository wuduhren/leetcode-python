"""
Time: O(N)
Space:O(LogN), for recursion stack space.
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
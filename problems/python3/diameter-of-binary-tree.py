"""
Time: O(N)
Space: O(LogN) for the recursion stack. If the tree is balanced.
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node: return 0
            l = helper(node.left)
            r = helper(node.right)
            self.ans = max(self.ans, 1+l+r)
            return 1+max(l, r)
        
        self.ans = 0
        
        helper(root)
        return self.ans-1
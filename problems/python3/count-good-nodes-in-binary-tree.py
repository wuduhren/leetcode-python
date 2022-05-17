"""
Time: O(N)
Space: O(LogN) for recursion stack if the tree is balanced.
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, maxVal):
            nonlocal count            
            if not node: return
            if node.val>=maxVal: count += 1
            helper(node.left, max(maxVal, node.val))
            helper(node.right, max(maxVal, node.val))
        
        count = 0
        helper(root, float('-inf'))
        return count
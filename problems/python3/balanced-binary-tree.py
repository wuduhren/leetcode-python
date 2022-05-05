"""
Time: O(N)
Space: O(LogN) Recursion stack. If the tree is balanced.
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(node) -> (bool, int):
            if not node: return True, 0
            leftIsBalanced, leftHeight = getHeight(node.left)
            if not leftIsBalanced: return False, 0
            
            rightIsBalanced, rightHeight = getHeight(node.right)
            if not rightIsBalanced: return False, 0
            
            return abs(leftHeight-rightHeight)<2, 1+max(leftHeight, rightHeight)
        
        isBalanced, h = getHeight(root)
        return isBalanced
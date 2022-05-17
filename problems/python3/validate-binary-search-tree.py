"""
The inorder travsersal of a BST is always increasing.

Time: O(N)
Space: O(N)
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lastVal = float('-inf')
        stack = []
        
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            
            if not lastVal<node.val: return False
            lastVal = node.val
            
            node = node.right
        return True
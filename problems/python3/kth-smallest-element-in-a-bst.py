"""
Time: O(N) for the inorder traversal
Space: O(LogN) if the tree is balanced.
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        stack = []
        node = root
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            
            count += 1
            if count==k: return node.val
            
            node = node.right
        return 0
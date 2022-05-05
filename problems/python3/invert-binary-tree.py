"""
Recursive
Time: O(N)
Space: O(LogN)
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        left = root.left
        right = root.right
        root.left = self.invertTree(right)
        root.right = self.invertTree(left)
        return root


"""
Iterative
Time: O(N)
Space: O(N)
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        q = collections.deque([root])
        
        while q:
            node = q.popleft()
            left = node.left
            right = node.right
            node.right = left
            node.left = right
            
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        
        return root
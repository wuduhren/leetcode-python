"""
Time: O(N)
Space: O(LogN) if the tree is balanced.

BFS is a more intuitive way to do this, but the time complexity will be at least O(N).
Using recursion instead, will take O(LogN) for the recursion stack size.
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node, level):
            if not node: return
            if len(ans)<level: ans.append(node.val)
            helper(node.right, level+1)
            helper(node.left, level+1)
        
        ans = []
        helper(root, 1)
        return ans
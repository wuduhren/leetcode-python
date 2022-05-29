"""
helper(node) will return the max path sum from the node to the leaf. [0]

Along the way we update the ans. [1]
The path of ans must pass through one of the node in the tree.
`node.val+left+right` means the max path sum that pass through the node.
So after all `helper()` is executed, we tested all the nodes.

Since there are some negative values in the tree, each node can decided not to take the negative path sum into account. [3]

Time: O(N)
Space: O(LogN) for the recursive stack (if the tree is balanced).
"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal ans
            
            if not node: return 0
            left = max(helper(node.left), 0) #[3]
            right = max(helper(node.right), 0) #[3]
            ans = max(ans, node.val+left+right) #[1]
            return node.val+max(left, right) #[0]
        
        ans = float('-inf')
        helper(root)
        return ans
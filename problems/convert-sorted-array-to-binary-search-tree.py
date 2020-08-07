class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums: return None
        
        m = len(nums)/2
        root = TreeNode(nums[m], self.sortedArrayToBST(nums[:m]), self.sortedArrayToBST(nums[m+1:]))
        return root


"""
`nums` is a sorted array.
To construct the most balanced BST, we must use the median number in `nums` as root.
So the number of elements under left subtree and right subtree will be the same.

Now we know which element in the `nums` will be root.
For `root.left` we only need to consider `nums[:m]`.
For `root.right` we only need to consider `nums[m+1:]`.
Which needs to be a balanced BST, too. So we apply the same logic.

Time: O(N). Because there will be N element being construct.
Space: O(LogN). There will be LogN level of recursive call.
"""
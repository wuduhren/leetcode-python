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



"""
Time: O(N)
Space: O(LogN)

To make it height-balanced
We need to make sure that the number of nodes in left substree and right subtree be the same.
Since the `nums` is already sorted, the best nodes to be root is the one in the middle.

`helper()` will get the root node from the nums[i:j].
If it has left child, it will recursively call `helper()` to get the child.

Use pointers i and j as param to avoid keep copying `nums`.
"""
class Solution(object):
    def sortedArrayToBST(self, nums):
        def helper(i, j):
            m = (i+j)/2
            node = TreeNode(nums[m])
            
            leftLength = m-i #number of nodes in the left subtree
            rightLength = j-(m+1) #number of nodes in the right subtree
            
            if leftLength>0: node.left = helper(i, m)
            if rightLength>0: node.right = helper(m+1, j)
            return node
        
        return helper(0, len(nums))




class Solution(object):
    def sortedArrayToBST(self, nums):
        def helper(s, e):
            if s>e: return None
            m = (s+e)/2
            node = TreeNode(nums[m])
            node.left = helper(s, m-1)
            node.right = helper(m+1, e)
            return node
        return helper(0, len(nums)-1)
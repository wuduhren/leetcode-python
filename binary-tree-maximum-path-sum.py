"""
For every subtree, we generate two output.

* The output from the path which can be used by its parent.
    * Only the node itself
    * The node with its avaliable left branch
    * The node with its avaliable right branch

* The output from the path which cannot (or won't) be used by its parent.
    * Only the path from the left branch
    * Only the path from the right branch
    * The node with avaliable left branch and avaliable right branch at the same time
    * The output of the first case. The means that even the path can be selected but we do not select it. Because selecting it will generate smaller output.

We initial all the value to be negative infinity, so the it will just be ignored by the `max()` if left or right node is `None`.
`a` means avaliable.
`na` means not avaliable.
"""
#recursive
class Solution(object):
    def maxPathSum(self, root):
        def helper(node):
            left_a = left_na = right_a = right_na = float('-inf')

            if node.left:
                left_a, left_na = helper(node.left)
            if node.right:
                right_a, right_na = helper(node.right)

            a = max(node.val, node.val+left_a, node.val+right_a)
            na = max(left_na, right_na, node.val+left_a+right_a, a)
            return a, na

        return max(helper(root))

#iterative
class Solution(object):
    def maxPathSum(self, root):
        pre_stack = [root]
        stack = []
        memo = {}

        while pre_stack:
            node = pre_stack.pop()
            stack.append(node)
            if node.left:
                pre_stack.append(node.left)
            if node.right:
                pre_stack.append(node.right)

        while stack:
            node = stack.pop()

            left_a = left_na = right_a = right_na = float('-inf')

            if node.left:
                left_a, left_na = memo[node.left]
            if node.right:
                right_a, right_na = memo[node.right]

            a = max(node.val, node.val+left_a, node.val+right_a)
            na = max(left_na, right_na, node.val+left_a+right_a, a)

            memo[node] = (a, na)

        return max(memo[root])


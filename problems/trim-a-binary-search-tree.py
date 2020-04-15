class Solution(object):
    def trimBST(self, root, L, R):
        if not root: return root
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root if L<=root.val and root.val<=R else root.left or root.right

"""
First, trim left child and right child.
Second, if the root is in range, return the root.
if not, return the trimed left child.
if not trimed left child, return the trimed right child.
if both left and right child is None, it will return None anyway.

Time complexity is O(N). For we simply just traverse all the nodes.
Space complexity is O(N). In the worst case, the recursion will go O(N) level deep.
"""
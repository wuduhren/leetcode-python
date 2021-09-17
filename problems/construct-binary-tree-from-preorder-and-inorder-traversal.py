"""
Time: O(N)
Space: O(N)

preorder: root[LEFT][RIGHT]
inorder: [LEFT]root[RIGHT]

The `helper()` will return the root node from `preorder` and `inorder`.
If they have left or right child, call `helper()` again to get the left or right node.

Use pointers to represent array, avoiding keep copying `preorder` and `inorder`.
i and j represent the preorder[i:j]
k and l epresent the inorder[k:l]
"""
class Solution(object):
    def buildTree(self, preorder, inorder):
        def helper(i, j, k, l):
            root = TreeNode(preorder[i])
            
            r = inorderIndex[root.val] #the index of the root val in inorder
            leftLength = r-k
            rightLength = l-(r+1)
            
            if leftLength>0: root.left = helper(i+1, i+1+leftLength, k, k+leftLength)
            if rightLength>0: root.right = helper(i+1+leftLength, i+1+leftLength+rightLength, r+1, r+1+rightLength)
            return root
        
        inorderIndex = {}
        for i, n in enumerate(inorder): inorderIndex[n] = i
        return helper(0, len(preorder), 0, len(inorder))
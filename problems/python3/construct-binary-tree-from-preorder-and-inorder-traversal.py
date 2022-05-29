"""
preorder: [root][left][right]
inorder:  [left][root][right]

[0]
As you can see, the root is always located at the first index of the preorder list.

[2]
Using the same logic, we can recursively get the left and right node
Inorder to do that, we need to define left and right nodes' range.
And we can get the length of the left subtree by locating the index of the root in the in order list. [1]
i and j is the startIndex and the (endIndex+1) of the preorder list.
k and l is the startIndex and the (endIndex+1) of the inorder list.

Time: O(N)
Space: O(N)
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(i, j, k, l):
            if i==j or k==l: return None
            
            root = TreeNode(preorder[i]) #[0]
            
            rootInorderIndex = getInorderIndex[root.val] #[1]
            leftLen = rootInorderIndex-k
            
            root.left = helper(i+1, i+1+leftLen, k, k+leftLen) #[2]
            root.right = helper(i+1+leftLen, j, rootInorderIndex+1, l)
            return root
        
        getInorderIndex = {}
        for i, v in enumerate(inorder): getInorderIndex[v] = i
        return helper(0, len(preorder), 0, len(inorder))
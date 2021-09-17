"""
inorder: [LEFT]root[RIGHT]
postorder: [LEFT][RIGHT]root

First thing we know is the value of root, which is the last element of `postorder`.
Find the index of the root in `inorder`. So find out the interval of [LEFT] and [RIGHT] in `inorder`.

The length of the [LEFT] and [RIGHT] in `inorder` are the same with the length of the [LEFT] and [RIGHT] in `postorder`.
"""
class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder: return None
        
        root = TreeNode(postorder[-1])
        if len(inorder)==1: return root
        
        r = inorder.index(root.val)
        
        leftInOrder = inorder[:r]
        leftPostOrder = postorder[:r]
        rightInOrder = inorder[r+1:]
        rightPostOrder = postorder[r:len(postorder)-1]
        
        root.left = self.buildTree(leftInOrder, leftPostOrder)
        root.right = self.buildTree(rightInOrder, rightPostOrder)
        
        return root
"""
Time: O(NLogN). For each node, we need to do an iteration to its children. To be precise..
O(N) for constructing root.

O(N/2) for constructing root.left
O(N/2) for constructing root.right

O(N/4) for constructing root.left.left
O(N/4) for constructing root.left.right
O(N/4) for constructing root.right.left
O(N/4) for constructing root.right.right
...

To improve this, we can use a hash table to get the index of `i` below


Space: O(NLogN).
For each node, we need to construct inorder/postorder arrays of its children.
We can improve this by using pointers.
"""

"""
Improved version.
Time: O(N).
Space: O(N). For `index`.
"""
class Solution(object):
    def buildTree(self, inorder, postorder):
        def helper(i, j, k, l):
            if j-i<=0: return None
            if l-k<=0: return None
            
            root = TreeNode(postorder[l-1])
            if j-i==1: return root

            r = index[root.val]
            
            root.left = helper(i, r, k, k+r-i)
            root.right = helper(r+1, j, k+r-i, l-1)
            return root
        
        index = {} #the index of inorder
        for i, n in enumerate(inorder): index[n] = i
        return helper(0, len(inorder), 0, len(postorder))
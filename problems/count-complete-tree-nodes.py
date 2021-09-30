"""
Time: O(H^2). The time complexity will countNodes() will be LogH if the tree is perfect.
If not, we will need Log(H-1)

Space: O(H)
"""
class Solution(object):
    def countNodes(self, root):
        if not root: return 0
        
        node = root
        l = 1 #level on the right side
        while node.left:
            node = node.left
            l += 1
        
        node = root
        r = 1 #level on the left side
        while node.right:
            node = node.right
            r += 1
        
        if l==r:
            #perfect tree
            return (2**r)-1
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
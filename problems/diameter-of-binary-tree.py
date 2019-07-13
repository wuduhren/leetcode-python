#https://leetcode.com/problems/diameter-of-binary-tree/
#what we want to find?
#max depth that goes right add max depth that goes left
#it could be from any node
#so we iterate through every node to update our the diameter to max

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        
        def traverse(node):
            if not node: return 0
            
            #the max depth go left from this node
            #the max depth go right from this node
            left, right = traverse(node.left), traverse(node.right)
            
            #update diameter if left+right is bigger
            self.diameter = max(self.diameter, left+right)
            
            #add 1 is for the step that get to this node
            #max(left, right) is for the left or right path that goes to the deepest
            return max(left, right)+1
        
        #iterate through the tree
        traverse(root)
        return self.diameter
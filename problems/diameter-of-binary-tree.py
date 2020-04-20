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

#2020
class Solution(object):
    def diameterOfBinaryTree(self, root):
        def getMaxDepth(node):
            if not node: return 0

            l, r = getMaxDepth(node.left), getMaxDepth(node.right)
            self.ans = max(self.ans, l+r)
            return max(l, r)+1 #add the node it self

        if not root: return 0
        self.ans = float('-inf')
        getMaxDepth(root)
        return self.ans
"""
What we want to find?
From an unknown node, that its max_depth_from_left (`l`) + max_depth_from_right (`r`) is the biggest.
The node that generate this number could be from any node, so we iterate through every node to update `ans`.
In other words, to find the answer, we need to check every node, if the max diameter pass through here.

Time complexity is O(N), where N is the number of nodes.
Space complexity is O(LogN), since we might got to LogN level on recursion.
"""

# from collections import defaultdict
# class Solution(object):
#     def diameterOfBinaryTree(self, root):
#         def getLeftLength(node):
#             if not node: return -1
#             if not (node in record and 'left' in record[node]):
#                 record[node]['left'] = max(getLeftLength(node.left), getRightLength(node.left))+1
#             return record[node]['left']
            
#         def getRightLength(node):
#             if not node: return -1
#             if not (node in record and 'right' in record[node]):
#                 record[node]['right'] = max(getLeftLength(node.right), getRightLength(node.right))+1
#             return record[node]['right']
        
#         if not root: return 0
        
#         record = defaultdict(dict)
#         ans = float('-inf')
#         stack = []
#         stack.append(root)
        
#         while stack:
#             node = stack.pop()
#             if not node: continue
            
#             d = getLeftLength(node)+getRightLength(node)
#             ans = max(ans, d)
#             stack.append(node.left)
#             stack.append(node.right)
            
#         return ans


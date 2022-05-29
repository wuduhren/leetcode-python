"""
Recursivly get the average and count of each node.
Update the self.ans before returning.

Time: O(N), N is the number of nodes.
Space: O(LogN) for the recursive stack, since the tree hight is LogN if the tree is balanced.
"""
class Solution(object):
    def __init__(self):
        self.ans = float('-inf')
        
    def maximumAverageSubtree(self, root):
        def getAVGAndCount(node):
            if not node: return 0, 0
            leftAvg, leftCount = getAVGAndCount(node.left)
            rightAvg, rightCount = getAVGAndCount(node.right)
            
            count = leftCount+rightCount+1
            avg = (leftAvg*leftCount + rightAvg*rightCount + node.val)/float(count)
            
            self.ans = max(self.ans, avg)
            return avg, count
        
        getAVGAndCount(root)
        return self.ans
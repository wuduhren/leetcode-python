"""
Time: O(N) for recursively traverse each node once.
Space: O(LogN) for recursive stack.
"""
class Solution(object):
    def largestBSTSubtree(self, root):
        def helper(node, minVal, maxVal):
            if not node: return True, 0, float('-inf'), float('inf')
            if not node.left and not node.right: return True, 1, node.val, node.val
            
            isLeftBST, leftSize, leftMin, leftMax = helper(node.left, minVal, node.val)
            isRightBST, rightSize, rightMin, rightMax = helper(node.right, node.val, maxVal)
            
            currMin = min(leftMin, rightMin, node.val)
            currMax = max(leftMax, rightMax, node.val)
            
            if isLeftBST and isRightBST and leftMax<node.val and node.val<rightMin:
                return True, 1+leftSize+rightSize, currMin, currMax
            else:
                return False, max(leftSize, rightSize), currMin, currMax
            
        return helper(root, float('-inf'), float('inf'))[1]
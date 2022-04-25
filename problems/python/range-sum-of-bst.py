class Solution(object):
    def rangeSumBST(self, root, low, high):
        def helper(node, low, high):
            total = 0
            if not node: return total
            if low<=node.val<=high: total += node.val
            if node.val<=high: total += helper(node.right, low, high)
            if node.val>=low: total += helper(node.left, low, high)
            return total
        
        return helper(root, low, high)
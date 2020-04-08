"""
The tree is balanced if
1. Left child and right child are balanced
2. |left_max_depth - right_max_depth| must smaller or equal to 1

So the helper() will check condition 1. and 2. by `if l!=-1 and r!=-1 and abs(l-r)<=1`
if true, the node is balanced, return the depth
if not, the node is not balanced, return -1
"""
class Solution(object):
    def isBalanced(self, root):

        def helper(node, depth):
            if not node.left and not node.right: return depth
            
            l = r = depth #l: left_max_depth, r: right_max_depth
            if node.left:
                l = helper(node.left, depth+1)
            if node.right:
                r = helper(node.right, depth+1)

            if l!=-1 and r!=-1 and abs(l-r)<=1:
                return max(l, r)
            return -1
        
        if not root: return True
        return helper(root, 0)!=-1
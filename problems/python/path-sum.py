class Solution(object):
    def hasPathSum(self, root, S):
        if not root: return False
        
        stack = []
        stack.append((root, 0))
        
        while stack:
            node, s = stack.pop()
            s += node.val
            if not node.left and not node.right and s==S: return True
            if node.left: stack.append((node.left, s))
            if node.right: stack.append((node.right, s))
        return False


"""
Time: O(N)
Space: O(N)

DFS
"""
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root: return False
        
        stack = [(root, root.val)]
        
        while stack:
            node, total = stack.pop()
            
            if not node.left and not node.right and total==targetSum: return True
            if node.left: stack.append((node.left, total+node.left.val))
            if node.right: stack.append((node.right, total+node.right.val))
            
        return False
        
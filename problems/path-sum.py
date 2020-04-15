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
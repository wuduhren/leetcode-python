class Solution(object):
    def binaryTreePaths(self, root):
        if not root: return []
        
        arrow = '->'

        ans = []
        stack = []
        stack.append((root, ''))

        while stack:
            node, path = stack.pop()
            path += arrow+str(node.val) if path else str(node.val) #add arrow except beginnings
            if not node.left and not node.right: ans.append(path) #if isLeaf, append path.
            if node.left: stack.append((node.left, path))
            if node.right: stack.append((node.right, path))

        return ans
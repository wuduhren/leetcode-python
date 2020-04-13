class Solution(object):
    def isUnivalTree(self, root):
        stack = []
        stack.append(root)
        value = root.val
        while stack:
            node = stack.pop()
            if node.val!=value: return False
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return True
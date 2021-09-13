"""
Time: O(N)
Time: O(N)
"""
class Solution(object):
    def invertTree(self, root):
        if not root: return root
        q = collections.deque([root])
        
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        
        return root
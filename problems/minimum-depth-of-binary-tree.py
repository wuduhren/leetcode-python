"""
We use BFS, so as soon as we touch a leaf; we can return it.
Because BFS traverse the tree level by level. We can be sure that the first leaf we touch is the nearest leaf.
Note that, a leaf is a node with no children.
"""
from collections import deque

class Solution(object):
    def minDepth(self, root):
        if not root: return 0
        q = deque()
        q.append((root, 1))
        
        while q:
            node, depth = q.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
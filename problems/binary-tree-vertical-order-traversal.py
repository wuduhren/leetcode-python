"""
Time: O(N)
Space: O(N)

Use BFS to traverse the tree.
x is the x coordinate of the node, the smaller the x is the leftmost node will be.
Since we add the left node first, the nodes "in the same row and column" will automatically sorted from left to right.
"""
class Solution(object):
    def verticalOrder(self, root):
        if not root: return []
        
        q = collections.deque([(root, 0)])
        minX = 0
        maxX = 0
        ans = collections.defaultdict(list)
        
        while q:
            node, x = q.popleft()
            ans[x].append(node.val)
            minX = min(minX, x)
            maxX = max(maxX, x)
            
            if node.left: q.append((node.left, x-1))
            if node.right: q.append((node.right, x+1))
            
        return [ans[x] for x in xrange(minX, maxX+1)]
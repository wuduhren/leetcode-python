"""
Time complexity: O(N), N is the number of nodes. Becasue we use DFS to traverse all the nodes.
Space complexity: O(N), N is the number of nodes. Becasue the stack may potentially store all the nodes.
"""
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        
        stack = []
        stack.append((root, 1))
        max_depth = 0
        
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        return max_depth


"""
Time: O(N)
Space: O(N)

Standard BFS.
"""
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        
        ans = float('-inf')
        q = collections.deque([(root, 1)])
        node = root
        
        while q:
            node, d = q.popleft()
            
            ans = max(ans, d)
            
            if node.left: q.append((node.left, d+1))
            if node.right: q.append((node.right, d+1))
        
        return ans
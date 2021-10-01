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


"""
Time: O(N)
Space: O(N)

Standard BFS.
"""
class Solution(object):
    def binaryTreePaths(self, root):
        q = collections.deque([(root, '')])
        ans = []
        
        while q:
            node, path = q.popleft()
            
            path = (path+'->'+str(node.val)) if path else str(node.val)
            
            if node.left: q.append((node.left, path))
            if node.right: q.append((node.right, path))

            if not node.left and not node.right: ans.append(path)
            
        return ans
from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
        opt = []

        if not root: return opt

        q = deque()
        q.append((root, 0))

        while q:
            node, depth = q.popleft()
            if depth<len(opt):
                opt[depth].append(node.val)
            else:
                opt.append([node.val])
            if node.left: q.append((node.left, depth+1))
            if node.right: q.append((node.right, depth+1))
        return reversed(opt)


"""
Time: O(N).
Space: O(N).

Simply using BFS, adding node and the level to the queue.
When popping out append the val to the correct list.
"""
class Solution(object):
    def levelOrderBottom(self, root):
        if not root: return []
        ans = []
        q = collections.deque([(root, 0)])
        
        while q:
            node, level = q.popleft()
            if len(ans)<level+1: ans.append([])
            ans[level].append(node.val)
            
            if node.left: q.append((node.left, level+1))
            if node.right: q.append((node.right, level+1))
        
        return reversed(ans)

"""
Time: O(N).
Space: O(N).

In the for-loop, it will pop all the nodes in the same level out at and add children to it.
Somehow this method is much faster.
"""
class Solution(object):
    def levelOrderBottom(self, root):
        if not root: return []
        ans = []
        q = collections.deque([root])
        
        while q:
            ans.append([])
            currLevelCount = len(q)
            for _ in xrange(currLevelCount):
                node = q.popleft()
                ans[-1].append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return reversed(ans)
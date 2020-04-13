from collections import deque

class Solution(object):
    def levelOrder(self, root):
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
        return opt

"""
Time complexity is O(N). Because we perform a BFS, where N is the number of nodes. (We traverse all the nodes in the tree)
Time complexity is O(N), too. Because we might potentially store all the nodes in the queue.
"""
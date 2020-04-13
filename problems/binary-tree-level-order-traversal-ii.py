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
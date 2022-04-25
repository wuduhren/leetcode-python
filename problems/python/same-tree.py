from collections import deque

class Solution(object):
    def isSameTree(self, p, q):
        q1 = deque([p])
        q2 = deque([q])
        while q1 or q2:
            if not q1 or not q2: return False
            n1 = q1.popleft()
            n2 = q2.popleft()
            
            if n1 and n2:
                if n1.val!=n2.val: return False
                q1.append(n1.left)
                q1.append(n1.right)
                q2.append(n2.left)
                q2.append(n2.right)
            elif n1 and not n2:
                return False
            elif not n1 and n2:
                return False
        return True


"""
Time: O(N)
Space: O(N)

Use BFS to traverse the tree and represent the result as a string.
Note that null node still need to be shown in the string.
Because there are the same val in the tree, and different tree may result in the same string.
"""
class Solution(object):
    def isSameTree(self, p, q):
        def getStr(node):
            s = ''
            q = collections.deque([node])
            
            while q:
                node = q.popleft()
                if not node:
                    s += '#'
                else:
                    s += str(node.val)
                    q.append(node.left)
                    q.append(node.right)
            return s
        
        return getStr(p)==getStr(q)
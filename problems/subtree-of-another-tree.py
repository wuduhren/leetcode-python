"""
We use DFS to traverse `s`. (Or you can use BFS)
If we encounter a node and `node.val==t.val`.
We check if the node and t are the same tree, using `isSameTree()`.

In `isSameTree()` we use BFS to traverse both tree to check if they are exactly the same.
We use BFS because. If some nodes are not the same, we can return early at higher level.
Do need to go deep. Imagine the node that is not the same is at the bottom of the tree...

Time complexity is O(M*N). M is the number of nodes in s. N is the number of nodes in t.
Traversing s takes O(M).
`isSameTree()` takes O(N) to check all nodes in t.
In the worst case, we might need to execute `isSameTree()` on every node in s.

Space complexity is O(M+N), since we might store all the nodes in memory.
"""
from collections import deque

class Solution(object):
    def isSubtree(self, s, t):
        def isSameTree(root1, root2):
            q1 = deque([root1])
            q2 = deque([root2])
            while q1 and q2:
                n1 = q1.popleft()
                n2 = q2.popleft()
                if n1.val!=n2.val: return False
                if n1.left: q1.append(n1.left)
                if n1.right: q1.append(n1.right)
                if n2.left: q2.append(n2.left)
                if n2.right: q2.append(n2.right)

            #check if both queue are empty.
            #if both queue are empty, all nodes are checked.
            return not q1 and not q2

        stack = []
        stack.append(s)
        while stack:
            node = stack.pop()
            if node.val==t.val and isSameTree(node, t): return True
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return False
"""
perform BFS to the tree:
we traverse every node in the level then go to the next level
every level we traverse from right to left
if it is a level we haven't been through before
we add the node's val to the output

time efficiency is O(N)
because we basically go through all the nodes
N is the total nodes count

space efficiency is O(N)
since we my store the whole level of the tree in the queue
the last level is 0.5N
N is the total nodes count
"""
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        queue = deque([(root, 0)])
        max_level = -1
        view = []
        while queue:
            node, level = queue.popleft()
            if node==None: continue
            if level>max_level:
                max_level = level
                view.append(node.val)
            queue.append((node.right, level+1))
            queue.append((node.left, level+1))
        return view

"""
Time: O(N).
Space: O(N).

Similar solution using DFS.
"""
class Solution(object):
    def rightSideView(self, root):
        if not root: return []
        
        ans = []
        currLevel = -1
        stack = [(root, 0)]
        
        while stack:
            node, level = stack.pop()
            if level>currLevel:
                ans.append(node.val)
                currLevel = level
            if node.left: stack.append((node.left, level+1))
            if node.right: stack.append((node.right, level+1))
                
        return ans
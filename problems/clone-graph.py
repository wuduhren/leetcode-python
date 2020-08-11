"""
approach 2 is more easy to understand
but approach 1 is better, since it only iterate once
both of them are O(N) in time efficiency and O(N) in space efficiency

1.
in 'clone' we store original and clone node as key value pair [0]
in 'stack' we store the original node which its clone is generated but the clone's neighbors isn't set yet [1]
we pop the node in the stack and set its clone's neighbors [2]
if the neighbor is not generated before we generate a clone and push it to stack [3]
by this way we are basically traverse the graph by DFS

2.
we traverse every node in the graph
if a node's neighbor is not in clone, which means it hasn't been visit yet, we add it to stack
by this way we have every node and its clone in the 'clone' dictionary now [0]

we iterate every node in the clone and setup its neighbors [1]
"""
class Solution(object):
    def cloneGraph(self, start):
        if start==None: return start
        clone = {} #[0]
        stack = [] #[1]
        
        clone[start] = Node(start.val, [])
        stack.append(start)
        
        while stack:
            node = stack.pop()
            for nb in node.neighbors:
                if nb not in clone: #[3]
                    clone[nb] = Node(nb.val, [])
                    stack.append(nb)
                clone[node].neighbors.append(clone[nb]) #[2]
                
        return clone[start]

class Solution(object):
    def cloneGraph(self, start):
        clone = {}
        stack = [start]
        
        while stack: #[0]
            node = stack.pop()
            if node not in clone:
                clone[node] = Node(node.val, [])
                for nb in node.neighbors:
                    stack.append(nb)
                
        for node in clone: #[1]
            for nb in node.neighbors:
                clone[node].neighbors.append(clone[nb])
                
        return clone[start]

#2020/8/7, similar to 2
class Solution(object):
    def cloneGraph(self, node):
        if not node: return node
        
        visited = set()
        clones = {}
        stack = []
        
        stack.append(node)
        while stack:
            curr = stack.pop()
            if curr in visited: continue
            visited.add(curr)
            clones[curr] = Node(curr.val)
            stack.extend(curr.neighbors)
        
        for curr in clones:
            clones[curr].neighbors = [clones[c] for c in curr.neighbors]
        
        return clones[node]
        









from collections import defaultdict

class Solution(object):
    def isBipartite(self, graph):
        if not graph: return True
        
        A, B = set(), set()
        stack = []
        
        for node in xrange(len(graph)): #[1]
            #check if visited, if not start DFS by putting it to stack
            if node not in A and node not in B:
                stack.append(node)
                A.add(node)
            
            while stack: #[0]
                n = stack.pop()
                if n in A:
                    for nei in graph[n]:
                        if nei in A: return False
                        if nei not in B:
                            stack.append(nei)
                            B.add(nei)
                elif n in B:
                    for nei in graph[n]:
                        if nei in B: return False
                        if nei not in A:
                            stack.append(nei)
                            A.add(nei)
        return True
"""
Use DFS to travserse each node [0]
If the node is in A, all its children should be in B.
If the node is in B, all its children should be in A.

Not necessary all the nodes in graph are connected. [1]
So we still need to loop the node to check if it is visited.
"""
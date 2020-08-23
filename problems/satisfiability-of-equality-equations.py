from collections import defaultdict

class Solution(object):
    def equationsPossible(self, equations):
        def isConnected(n1, n2):
            if n1==n2: return True
            
            stack = [n1]
            visited = set()
            
            while stack:
                n = stack.pop()
                if n in visited: continue
                visited.add(n)
                
                if n==n2: return True
                
                stack.extend(graph[n])
            return False
        
        not_equals = set()
        graph = defaultdict(list)
        
        #build graph
        for e in equations:
            if e[1:3]=='==':
                graph[e[0]].append(e[3])
                graph[e[3]].append(e[0])
            elif e[1:3]=='!=':
                if (e[0], e[3]) not in not_equals and (e[3], e[0]) not in not_equals:
                    not_equals.add((e[0], e[3]))
        
        #find contradiction
        for n1, n2 in not_equals:
            if isConnected(n1, n2): return False
        
        return True

"""
For each `!=` equation, if we find two variables are equal (`isConnected()`), we return `False`.
Otherwise, we return `True`.

[build graph]
First, lets build the graph.
Variables in the same graph means they are all equal.

[find contradiction]
Second, we find if any "!=" variables (`n1` and `n2`) exist in the same graph.
Starting from `n1`, if we can find `n2` through DFS, they have the same value.

Time: O(EV).
Building the graph takes O(E). Finding contradiction takes O(EV).
E is the number of edges, in this case, `len(equations)`.
V is the number of nodes, in this case, the unique variables in the equations.

Space: O(V). For the graph.
"""
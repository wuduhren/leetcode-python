"""
I learn the solution from @mlaw0.
He used BFS, so I use DFS. The runtime is almost the same.
But I think BFS is more suitable in this case, bc we don't have to go down that deep.

we know if a/b=2, b/c=3, then
1. b/a=1/2, c/b=1/3 [2]
2. a/c=2*3, becasue (a/b)*(b/c)=a/c=2*3
we can build graph: a->(b, 2), b->(c, 3).
a->(b, 2) means a-->2-->b
b->(c, 3) means b-->3-->c
so if we need a/c, we are finding a-->?-->c, which is a-->2-->b-->3-->c, which is a-->2*3-->c

first we build the graph [0]
for every query, we find from the starting point (n1) itself [1]
in the stack is the next thing we want to check if it is n2
we keep on pushing neighbor or neighbor's neighbor to the stack until we find n2 [3]

to prevent we visit the visited node we use a set to keep track [4]

we can further optimize the answer by updating the graph at the same time
bc it is not likely that we build the graph for a single search [5]
"""
class Solution(object):
    def calcEquation(self, equations, values, queries):
        def findVal(query):
            n1, n2 = query
            if n1 not in graph or n2 not in graph: return -1.0
            
            stack = [(n1, 1.0)] #[1]
            visited = set() #[4]
            
            while stack:
                n, val = stack.pop()
                visited.add(n)
                if n==n2:
                    return val
                else:
                    for nb, nb_val in graph[n]: #nb means neighbor
                        if nb not in visited:
                            stack.append((nb, nb_val*val)) #[3]
                            if n!=n1: graph[n1].append((nb, nb_val*val)) #[5]
            return -1.0
            
        def addEdge(n1, n2, val):
            if n1 in graph:
                graph[n1].append((n2, val))
            else:
                graph[n1] = [(n2, val)]
        
        #[0]
        graph = {}
        for (n1, n2), val in zip(equations, values):
            addEdge(n1, n2, val)
            addEdge(n2, n1, 1/val)

        return [findVal(query) for query in queries]


from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
		#using DFS
        def find_val(n1, n2):
            if n1 not in graph or n2 not in graph: return -1
            if n1==n2: return 1
            if n2 in graph[n1]: return graph[n1][n2]
                
            stack = [(n1, 1)]
            visited = set()
            
            while stack:
                n, v = stack.pop() #v is the val of n1/n
				
                if n in visited: continue
                visited.add(n)
                
                if n==n2:
                    graph[n1][n2] = v
                    return v
                
                stack.extend([(next_n, v*graph[n][next_n]) for next_n in graph[n]])
            return -1
        
        #build graph
        graph = defaultdict(dict)
        for i, v in enumerate(values):
            n1, n2 = equations[i][0], equations[i][1]
            graph[n1][n2] = v
            graph[n2][n1] = 1/v
        
        ans = []
        for n1, n2 in queries:
            ans.append(find_val(n1, n2))
            
        return ans
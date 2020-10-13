#DFS
"""
For each edge (u, v), traverse the graph with a depth-first search to see if we can connect u to v. If we can, then it must be the duplicate edge.
Time Complexity: O(N^2)
Space Complexity: O(N)
"""
from collections import defaultdict

class Solution(object):
    def findRedundantConnection(self, edges):
        def dfs(u, v):
            seen = set()
            stack = []
            stack.append(u)
            
            while stack:
                node = stack.pop()
                seen.add(node)
                
                if v in G[node]: return True
                
                for nei in G[node]:
                    if nei not in seen:
                        stack.append(nei)
            return False
            
        G = defaultdict(set)
        
        for u, v in edges:
            if u in G and v in G and dfs(u, v): return u, v
            G[u].add(v)
            G[v].add(u)

#Disjoint Set Union
"""
For Disjoint Set Union, see
https://www.youtube.com/watch?v=ID00PMy0-vE
Time Complexity: O(N)
Space Complexity: O(N)
"""
class DSU(object):
    def __init__(self):
        self.parant = range(1001)
        self.rank = [0]*1001
    
    def find(self, x):
        if self.parant[x]!=x:
            self.parant[x] = self.find(self.parant[x])
        return self.parant[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr==yr:
            return False
        elif self.rank[xr]>self.rank[yr]:
            self.parant[yr] = xr
            self.rank[xr] += 1
        else:
            self.parant[xr] = yr
            self.rank[yr] += 1
        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge

#Disjoint Set Union without Ranking
"""
Time Complexity: O(N)
Space Complexity: O(N)
"""
class DSU(object):
    def __init__(self):
        self.parant = range(1001)
    
    def find(self, x):
        if self.parant[x]!=x:
            self.parant[x] = self.find(self.parant[x])
        return self.parant[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr==yr: return False
        self.parant[yr] = xr
        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge
class Solution(object):
    def countComponents(self, N, edges):
        def dfs(start):
            stack = [start]
            
            while stack:
                node = stack.pop()
                if node in visited: continue
                visited.add(node)
                
                for nei in g[node]:
                    stack.append(nei)
                    
        g = collections.defaultdict(list)
        visited = set()
        count = 0
        
        for n1, n2 in edges:
            g[n1].append(n2)
            g[n2].append(n1)
        
        for n in xrange(N):
            if n in visited: continue
            dfs(n)
            count += 1
            
        return count


class Solution(object):
    def countComponents(self, n, edges):
        def find(n):
            p = parents[n]
            while p!=parents[p]:
                p = find(p)
            parents[n] = p
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1==p2: return False
            parents[p2] = p1
            return True
        
        count = n
        parents = [n for n in xrange(n)]
        
        for n1, n2 in edges:
            if union(n1, n2): count -= 1
        return count
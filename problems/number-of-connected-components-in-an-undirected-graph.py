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
            # print visited
            if n in visited: continue
            dfs(n)
            count += 1
            
        return count
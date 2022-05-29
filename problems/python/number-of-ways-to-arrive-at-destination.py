class Solution(object):
    def countPaths(self, n, roads):
        def countWaysToReach(node):
            if node==0: return 1
            if node in history: return history[node]
            c = 0
            for nei, t in adj[node]:
                if nei in times and times[nei]+t==times[node]:
                    c += countWaysToReach(nei)
            history[node] = c
            return c
        
        history = {} #cache for countWaysToReach()
        times = {} #min times to reach node n-1
        pq = [(0, 0)]
        
        adj = collections.defaultdict(list)
        for u, v, t in roads:
            adj[u].append((v, t))
            adj[v].append((u, t))
        
        while pq:
            t, node = heapq.heappop(pq)
            if node in times: continue
            times[node] = t
            
            if node==n-1: break
            
            for nei, t2 in adj[node]:
                if nei in times: continue
                heapq.heappush(pq, (t+t2, nei))
        
        return countWaysToReach(n-1)%(10**9 + 7)
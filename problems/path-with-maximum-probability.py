class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        pq = [(-1, start)]
        visited = set()
        adj = collections.defaultdict(list)
        for i in xrange(len(edges)):
            a, b = edges[i]
            p = succProb[i]
            adj[a].append((b, p))
            adj[b].append((a, p))
        
        while pq:
            p, node = heapq.heappop(pq)
            p = p*-1
            if node in visited: continue
            visited.add(node)
            
            if node==end: return p
            
            for nei, p2 in adj[node]:
                if nei in visited: continue
                heapq.heappush(pq, (-1*p*p2, nei))
        
        return 0
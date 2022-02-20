class Solution(object):
    def minimumCost(self, n, highways, discounts):
        pq = [(0, discounts, 0)]
        visited = set()
        
        adj = collections.defaultdict(list)
        for city1, city2, toll in highways:
            adj[city1].append((city2, toll))
            adj[city2].append((city1, toll))
        
        
        while pq:
            toll, d, city = heapq.heappop(pq)
            if (d, city) in visited: continue
            visited.add((d, city))
            
            if city==n-1: return toll
            
            for nei, toll2 in adj[city]:
                if (d, nei) not in visited:
                    heapq.heappush(pq, (toll+toll2, d, nei))
                if d>0 and (d-1, nei) not in visited:
                    heapq.heappush(pq, (toll+toll2/2, d-1, nei))    
        
        return -1
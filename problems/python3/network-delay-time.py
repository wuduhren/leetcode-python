class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ans = 0
        adj = collections.defaultdict(list)
        h = []
        visited = set()
        
        for u, v, w in times:
            adj[u].append((v, w))
            
        heapq.heappush(h, (0, k))
        while h:
            timeNeededToGetHere, node = heapq.heappop(h)
            
            if node in visited: continue
            visited.add(node)
            ans = max(ans, timeNeededToGetHere)
            
            for nei, time in adj[node]:
                if nei in visited: continue
                heapq.heappush(h, (time+timeNeededToGetHere, nei))
        
        return ans if len(visited)==n else -1
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ans = 0
        visited = set()
        adj = collections.defaultdict(list)
        N = len(points)
        
        #build adjacency list
        for i in range(N):
            x0, y0 = points[i]
            for j in range(i+1, N):
                x1, y1 = points[j]
                dis = abs(x0-x1)+abs(y0-y1)
                adj[(x0, y0)].append((dis, x1, y1))
                adj[(x1, y1)].append((dis, x0, y0))
        
        h = [(0, points[0][0], points[0][1])] #min heap
        while len(visited)<N:
            dis, x, y = heapq.heappop(h)
            
            if (x, y) in visited: continue
            visited.add((x, y))
            ans += dis
            
            for dis1, x1, y1 in adj[(x, y)]:
                if (x1, y1) in visited: continue
                heapq.heappush(h, (dis1, x1, y1))
        return ans
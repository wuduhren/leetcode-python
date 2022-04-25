class Solution(object):
    def trapRainWater(self, heightMap):
        pq = []
        N = len(heightMap)
        M = len(heightMap[0])
        visited = set()
        ans = 0
        curr = float('-inf')
        
        for i in xrange(N):
            for j in xrange(M):
                if i==0 or i==N-1 or j==0 or j==M-1:
                    heapq.heappush(pq, (heightMap[i][j], i, j))
                
        while pq:
            h, i, j = heapq.heappop(pq)
            if (i, j) in visited: continue
            visited.add((i, j))
            
            if h>curr: curr = h
            ans += (curr-h)
            
            for iNext, jNext in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if iNext<0 or iNext>=N or jNext<0 or jNext>=M: continue
                if (iNext, jNext) in visited: continue
                heapq.heappush(pq, (heightMap[iNext][jNext], iNext, jNext))
        
        return ans
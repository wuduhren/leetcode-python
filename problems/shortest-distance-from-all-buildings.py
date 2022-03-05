class Solution(object):
    def shortestDistance(self, grid):
        def bfs(i0, j0):
            q = collections.deque([(i0, j0, 0)])
            visited = set()
            while q:
                i, j, dis = q.popleft()
                if (i, j) in visited: continue
                visited.add((i, j))
                
                reach[i][j] += 1
                distances[i][j] += dis
                
                for iNext, jNext in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                    if not (0<=iNext<len(grid) and 0<=jNext<len(grid[0])): continue
                    if grid[iNext][jNext]==2 or grid[iNext][jNext]==1: continue
                    if (iNext, jNext) in visited: continue
                    q.append((iNext, jNext, dis+1))
        
        M = len(grid)
        N = len(grid[0])
        ans = float('inf')
        reach = [[0]*N for _ in xrange(M)] #number of buildings can reach (i, j)
        distances = [[0]*N for _ in xrange(M)] #aggregate distance btwn 0 and buildings.
        buildingCount = 0
        
        for i in xrange(M):
            for j in xrange(N):
                if grid[i][j]==1:
                    buildingCount += 1
                    bfs(i, j)
        
        
        for i in xrange(M):
            for j in xrange(N):
                if grid[i][j]==0 and reach[i][j]==buildingCount:
                    ans = min(ans, distances[i][j])
        
        return ans if ans!=float('inf') else -1
class Solution(object):
    def shortestPath(self, grid, K):
        N = len(grid)
        M = len(grid[0])
        
        q = collections.deque([(0, 0, 0, K)])
        qNext = collections.deque()
        visited = set()
        
        while q:
            step, i0, j0, k0 = q.popleft()
            if (i0, j0, k0) in visited: continue
            visited.add((i0, j0, k0))
            
            if i0==N-1 and j0==M-1: return step
            
            for i, j in [(i0+1, j0), (i0-1, j0), (i0, j0+1), (i0, j0-1)]:
                if i>=N or i<0 or j>=M or j<0: continue
                if grid[i][j]==1 and k0>0:
                    qNext.append((step+1, i, j, k0-1))
                elif grid[i][j]==0:
                    qNext.append((step+1, i, j, k0))
            if not q: q = qNext
        
        return -1
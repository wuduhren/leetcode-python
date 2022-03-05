class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        q = collections.deque([(0, 0, 1)])
        seen = 2
        
        while q:
            i, j, step = q.popleft()
            if not (0<=i<len(grid) and 0<=j<len(grid[0])): continue
            if grid[i][j]==1 or grid[i][j]==seen: continue
            grid[i][j] = seen
            
            if i==len(grid)-1 and j==len(grid[0])-1: return step
            
            for k, l in ((i+1, j), (i-1, j), (i, j+1), (i, j-1), (i-1, j-1), (i+1, j-1), (i+1, j+1), (i-1, j+1)):
                q.append((k, l, step+1))
        
        return -1
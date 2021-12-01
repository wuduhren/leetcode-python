class Solution(object):
    def getFood(self, grid):
        q = collections.deque()
        visited = set()
        
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j]=='*':
                    q.append((i, j, 0))
                    break
        while q:
            i, j, steps = q.popleft()
            
            if not 0<=i<len(grid): continue
            if not 0<=j<len(grid[0]): continue
            if (i, j) in visited: continue
            visited.add((i, j))
            
            if grid[i][j]=='#':
                return steps
            elif grid[i][j]=='X':
                continue
            elif grid[i][j]=='O' or grid[i][j]=='*':
                q.append((i+1, j, steps+1))
                q.append((i-1, j, steps+1))
                q.append((i, j+1, steps+1))
                q.append((i, j-1, steps+1))
        
        return -1
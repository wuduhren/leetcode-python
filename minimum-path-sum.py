"""
let's reset the array by it's min value start out from (0,0)
in another words, after reset
grid[i][j]'s value will be the min value start out from (0,0)

if we are at (i,j), we will be either from (i-1,j) or (i,j-1)
we call them s1 and s2, let's assume they are both in range
grid[i][j] will be grid[i][j]+min(s1, s2)

we will start out from (0,0) and reset the entire grid.
"""
class Solution(object):
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])
        for i in xrange(n):
            for j in xrange(m):
                s1 = s2 = float('inf')
                if i-1>=0:
                    s1 = grid[i-1][j]
                if j-1>=0:
                    s2 = grid[i][j-1]
                    
                if s1==float('inf') and s2==float('inf'): continue #both source out of range
                grid[i][j]+=min(s1, s2)
                
        return grid[-1][-1]
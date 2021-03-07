class Solution(object):
    def maximalSquare(self, grid):
        if not grid or not grid[0]: return 
        M, N = len(grid), len(grid[0])
        
        dp = [[0 for _ in xrange(N+1)] for _ in xrange(M+1)]
        ans = 0
        for i in xrange(M):
            for j in xrange(N):
                if grid[i][j]=='1':
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j])+1
                    ans = max(ans, dp[i+1][j+1])
        return ans**2
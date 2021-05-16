class Solution(object):
    def minScoreTriangulation(self, values):
        N = len(values)
        dp = [[float('inf')]*N for _ in xrange(N)]
        
        for i in xrange(N-1):
            dp[i][i+1] = 0
        
        for l in xrange(3, N+1):
            for i in xrange(N-l+1):
                j = i+l-1
                
                for k in xrange(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k]+values[i]*values[k]*values[j]+dp[k][j])
        return dp[0][N-1]
            
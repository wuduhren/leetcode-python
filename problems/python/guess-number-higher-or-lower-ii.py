"""
dp[i][j] := min money guarantee to win within i~j
k is the first guess, try all k and update dp[i][j].
"""
class Solution(object):
    def getMoneyAmount(self, N):
        dp = [[float('inf') for _ in xrange(N)] for _ in xrange(N)]
        for i in xrange(N): dp[i][i] = 0
        
        
        for l in xrange(2, N+1):
            for i in xrange(N):
                j = i+l-1
                if j>=N: continue
                for k in xrange(i, j+1):
                    dp[i][j] = min(dp[i][j], max(dp[i][k-1] if k-1>=0 else 0, dp[k+1][j] if k+1<N else 0) + (k+1))
        
        return dp[0][N-1]
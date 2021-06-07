"""
dp[i][k] := minimum difficulty of a k days job schedule, D[:i].
maxInRange[i][j] := max(D[i:j+1])
"""

class Solution(object):
    def minDifficulty(self, D, K):
        if not D or not K or K>len(D): return -1
        N = len(D)

        maxInRange = [[0 for _ in xrange(N)] for _ in xrange(N)]
        for i in xrange(N): maxInRange[i][i] = D[i]
        for l in xrange(2, N+1):
            for i in xrange(N):
                j = i+l-1
                if j>=N: continue
                maxInRange[i][j] = max(maxInRange[i+1][j-1], D[i], D[j])

        dp = [[float('inf') for _ in xrange(K+1)] for _ in xrange(N+1)]
        dp[0][0] = 0

        for i in xrange(1, N+1):
            for k in xrange(1, min(i, K)+1):
                for j in xrange(k, i+1):
                    dp[i][k] = min(dp[i][k], dp[j-1][k-1]+maxInRange[j-1][i-1])
                    
                    #if you don't pre-calculate maxInRange
                    #dp[i][k] = min(dp[i][k], dp[j-1][k-1]+max(D[j-1:i]))
        return dp[N][K]
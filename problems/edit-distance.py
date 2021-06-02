"""
dp[i][j] := minimum number of operations required to convert w1[:i] to w2[:j]
"""
class Solution(object):
    def minDistance(self, w1, w2):
        M, N = len(w1), len(w2)
        
        dp = [[0 for _ in xrange(N+1)] for _ in xrange(M+1)]
        
        for i in xrange(M+1): dp[i][0] = i
        for j in xrange(N+1): dp[0][j] = j
        
        for i in xrange(1, M+1):
            for j in xrange(1, N+1):
                if w1[i-1]==w2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)

        return dp[-1][-1]
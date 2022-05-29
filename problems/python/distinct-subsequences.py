"""
dp[i][j] := the number of distinct subsequences of s[:i] which equals t[:j]
"""
class Solution(object):
    def numDistinct(self, s, t):
        M, N = len(s), len(t)
        
        dp = [[0 for _ in xrange(N+1)] for _ in xrange(M+1)]
        for i in xrange(M+1): dp[i][0] = 1
        
        for i in xrange(1, M+1):
            for j in xrange(1, N+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]
"""
dp[i][j] := longest palindromic subsequence of s[i:j+1]
"""
class Solution(object):
    def longestPalindromeSubseq(self, s):
        N = len(s)

        dp = [[0 for _ in xrange(N)] for _ in xrange(N)]
        for i in xrange(N): dp[i][i] = 1

        for l in xrange(2, N+1):
            for i in xrange(N):
                j = i+l-1
                if j>=N: continue
                dp[i][j] = dp[i+1][j-1]+2 if s[i]==s[j] else max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][N-1]
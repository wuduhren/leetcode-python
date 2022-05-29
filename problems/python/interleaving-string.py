"""
dp[i][j] := whether s3[:i+j] is formed by an interleaving of s1[:i] and s2[:j]
"""
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if len(s1)+len(s2)!=len(s3): return False
        
        M, N = len(s1), len(s2)
        dp = [[False for _ in xrange(N+1)] for _ in xrange(M+1)]
        
        for i in xrange(M+1): dp[i][0] = s1[:i] == s3[:i]
        for j in xrange(N+1): dp[0][j] = s2[:j] == s3[:j]
        
        for i in xrange(1, M+1):
            for j in xrange(1, N+1):
                if s1[i-1]==s3[i+j-1] and dp[i-1][j]:
                    dp[i][j] = True
                elif s2[j-1]==s3[i+j-1] and dp[i][j-1]:
                    dp[i][j] = True
        
        return dp[-1][-1]
        
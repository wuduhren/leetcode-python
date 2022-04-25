"""
dp[i][j] := length of the scs of s1[:i] and s2[:j]
"""
class Solution(object):
    def shortestCommonSupersequence(self, s1, s2):
        N, M = len(s1), len(s2)
        
        if not s1: return s2
        if not s2: return s1
        
        dp = [[0 for _ in xrange(M+1)] for _ in xrange(N+1)]
        for i in range(1, N+1): dp[i][0] = i
        for j in range(1, M+1): dp[0][j] = j
        
        for i in xrange(1, N+1):
            for j in xrange(1, M+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)
        
        i, j = N, M
        ans = ''
        
        while i>0 and j>0:
            if s1[i-1]==s2[j-1]:
                ans = s1[i-1] + ans
                i -= 1
                j -= 1
            else:
                if dp[i][j-1]<dp[i-1][j]:
                    ans = s2[j-1] + ans
                    j -= 1
                else:
                    ans = s1[i-1] + ans
                    i -= 1

        if i>0: ans = s1[:i] + ans
        if j>0: ans = s2[:j] + ans

        return ans
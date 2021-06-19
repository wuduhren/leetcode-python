"""
dp[i][n][m] := max size of the subset with total m 0's and n 1's.
Find max size for each m<=M and n<=N.
"""
class Solution(object):
    def findMaxForm(self, strs, M, N):
        dp = [[[0 for _ in xrange(M+1)] for _ in xrange(N+1)] for _ in xrange(len(strs)+1)]
        
        for i in xrange(1, len(strs)+1):
            count0 = strs[i-1].count('0')
            count1 = len(strs[i-1])-count0

            for n in xrange(N+1):
                for m in xrange(M+1):
                    dp[i][n][m] = max(dp[i-1][n][m], (dp[i-1][n-count1][m-count0]+1) if m>=count0 and n>=count1 else 0)
        
        ans = 0
        for n in xrange(N+1):
                for m in xrange(M+1):
                    ans = max(ans, dp[-1][n][m])
            
        return ans
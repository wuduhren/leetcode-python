class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        N, M = len(s1), len(s2)
        dp = [[float('inf') for _ in xrange(M+1)] for _ in xrange(N+1)]
        
        dp[0][0] = 0
        
        for i in xrange(1, N+1):
            dp[i][0] = dp[i-1][0]+ord(s1[i-1])
            
        for j in xrange(1, M+1):
            dp[0][j] = dp[0][j-1]+ord(s2[j-1])
        
        for i in xrange(1, N+1):
            for j in xrange(1, M+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                dp[i][j] = min(dp[i][j], dp[i][j-1]+ord(s2[j-1]), dp[i-1][j]+ord(s1[i-1]))
        
        return dp[N][M]

"""
Time: O(MN)
Space: O(MN)
"""
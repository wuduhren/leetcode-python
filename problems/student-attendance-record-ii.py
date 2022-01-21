class Solution(object):
    def checkRecord(self, n):
        """
        dp[l] := number of eligible combination of a length l record without A
        """
        
        ans = 0
        M = 1000000007
        
        dp = [0]*max(n+1, 4)
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4
        dp[3] = 7
        
        for i in xrange(4, n+1):
            dp[i] += dp[i-1]%M #ends at P
            dp[i] += (dp[i-1]%M - dp[i-4]%M) #ends at L. All posiblity but the end cannot be PLL
        
        
        ans += dp[n]
        
        for i in xrange(n):
            ans += dp[i] * dp[n-i-1]
            ans %= M
            
        return ans
        
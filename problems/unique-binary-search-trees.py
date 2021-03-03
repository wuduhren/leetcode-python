
# Implement from https://www.youtube.com/watch?v=GgP75HAvrlY
class Solution(object):
    def numTrees(self, n):
        dp = [1, 1, 2]
        
        if n<=2: return dp[n]
        
        for i in xrange(3, n+1):
            dp.append(0)
            for root in xrange(1, i+1):
                dp[i] += dp[root-1]*dp[i-root]
                
        return dp[n]
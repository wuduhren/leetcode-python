#TLE
class Solution(object):
    def tallestBillboard(self, rods):
        D = sum(rods)
        N = len(rods)
        
        dp = [[float('-inf') for _ in xrange(-D, D+1)] for _ in xrange(N+1)]
        dp[0][D] = 0
        
        for i in xrange(1, N+1):
            for d in xrange(-D, D+1):
                h = rods[i-1]
                dp[i][d+D] = max(dp[i-1][d+D], (dp[i-1][d+D-h]+h) if d+D-h>=0 else float('-inf'), dp[i-1][d+D+h] if d+D+h<2*D+1 else float('-inf'))
        
        return dp[N][D]
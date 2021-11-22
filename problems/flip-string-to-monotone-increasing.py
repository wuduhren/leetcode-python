"""
dp[i][0] := min number of flips to form monotone string that ends s[:i] at 0
dp[i][1] := min number of flips to form monotone string that ends s[:i] at 1

Time: O(N)
Space: O(N), can further deduce to O(1)
"""
class Solution(object):
    def minFlipsMonoIncr(self, s):
        dp = [[0, 0] for _ in xrange(len(s)+1)]
        
        for i, c in enumerate(s):
            if c=='0':
                dp[i+1][0] = dp[i][0]
                dp[i+1][1] = min(dp[i][0], dp[i][1]) + 1
            elif c=='1':
                dp[i+1][0] = dp[i][0] + 1
                dp[i+1][1] = min(dp[i][0], dp[i][1])
                
        return min(dp[-1])
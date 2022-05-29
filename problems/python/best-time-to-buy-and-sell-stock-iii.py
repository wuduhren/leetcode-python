"""
dp[i][0~3] = max profit in ith day in 0~3 state.

0 hold the stock from 1th transaction.
1 sold the stock from 1th transaction.
2 hold the stock from 2nd transaction.
3 sold the stock from 2nd transaction.

dp[i][0] = max(-prices[i], dp[i-1][0])
dp[i][1] = max(dp[i-1][0]+prices[i], dp[i-1][1])
dp[i][2] = max(dp[i-1][1]-prices[i], dp[i-1][2])
dp[i][3] = max(dp[i-1][2]+prices[i], dp[i-1][3])

Time: O(N)
Space: O(N), can further reduce to O(1).
"""
class Solution(object):
    def maxProfit(self, prices):
        dp = [[0, 0, 0, 0] for _ in xrange(len(prices))]
        dp[0] = [-prices[0], 0, -prices[0], 0]
        
        for i in xrange(1, len(prices)):
            dp[i][0] = max(-prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0]+prices[i], dp[i-1][1])
            dp[i][2] = max(dp[i-1][1]-prices[i], dp[i-1][2])
            dp[i][3] = max(dp[i-1][2]+prices[i], dp[i-1][3])
                
        return max(dp[-1]) 
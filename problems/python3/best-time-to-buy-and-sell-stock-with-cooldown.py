#dp[i][0] := max profit when last action is buy
#dp[i][1] := max profit when last action is sell
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices)<=1: return 0
        
        N = len(prices)
        dp = [[0, 0] for _ in range(N)]
        dp[0] = [-prices[0], 0]
        dp[1][0] = max(-prices[1], -prices[0])
        dp[1][1] = max(prices[1]+dp[0][0], dp[0][1])
        
        for i in range(2, N):
            dp[i][0] = max(dp[i-2][1]-prices[i], dp[i-1][0])
            dp[i][1] = max(prices[i]+dp[i-1][0], dp[i-1][1])
        return max(dp[-1][0], dp[-1][1], 0)
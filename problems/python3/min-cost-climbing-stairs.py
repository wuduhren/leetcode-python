"""
Time: O(N)
Space: O(N), can further reduce to using only 2 variables -> O(1).

dp[i] := the cost to get to index i.
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        dp = [float('inf')]*(N+1)
        dp[0] = 0
        dp[1] = 0
        
        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[-1]
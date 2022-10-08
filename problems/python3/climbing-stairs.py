class Solution:
    def climbStairs(self, N: int) -> int:
        dp = [0]*(N+1)
        dp[0] = 1
        for i in range(len(dp)):
            if i-1>=0:
                dp[i] += dp[i-1]
            if i-2>=0:
                dp[i] += dp[i-2]
        return dp[-1]
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for coin in coins:
            if coin<len(dp): dp[coin] = 1
        
        coins.sort()
        
        for i in range(1, amount+1):
            for coin in coins:
                if i-coin<0: break
                dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount]!=float('inf') else -1
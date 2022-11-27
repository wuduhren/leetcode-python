class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        
        coins.sort()
        
        for coin in coins:
            for a in range(1, amount+1):
                if a-coin<0: continue
                dp[a] += dp[a-coin]
        return dp[-1]
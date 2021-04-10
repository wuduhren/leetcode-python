# DP
class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf')]*(amount+1)
        
        if amount==0: return 0
        
        dp[0] = 0
        for coin in coins:
            if coin<=amount:
                dp[coin] = 1
            
        for a in xrange(amount+1):
            for coin in coins:
                if a-coin>=0:
                    dp[a] = min(dp[a], dp[a-coin]+1)
                    
        return dp[amount] if dp[amount]!=float('inf') else -1

# BFS
import collections
class Solution(object):
    def coinChange(self, coins, amount):
        visited = set()
        
        coins.sort(reverse=True)
        q = collections.deque([(0, 0)])
        
        while q:
            current_amount, count = q.popleft()
            
            if current_amount==amount: return count
            if current_amount>amount: continue
            if current_amount in visited: continue
            visited.add(current_amount)
            
            for coin in coins:
                q.append((current_amount+coin, count+1))
        return -1
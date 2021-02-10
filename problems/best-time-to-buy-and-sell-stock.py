"""
To accomplish 0(N) solution:
For each i and price in the iteration, we need to keep track of the loest price before i.
Also, update the max_profit in the iteration.
"""
class Solution(object):
    def maxProfit(self, prices):
        if not prices: return 0
        max_profit = 0
        lowest = prices[0]
        
        for i in xrange(len(prices)):
            if i==0: continue
            max_profit = max(max_profit, prices[i]-lowest)
            lowest = min(lowest, prices[i])
        return max_profit
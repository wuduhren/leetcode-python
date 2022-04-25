"""
First setup a memo
The value in memo is the max profit we are going to get when we only look at 0~i
For every i, we either sell or not sell
* If we sell, the max profit is price now - lowest price before (prices[i]-min_price).
* If we not sell, the max profit we get now is the same as yesterday.
Every i between these two we pick the max.
So we iterate from 0 to the end.
"""
class Solution(object):
    def maxProfit(self, prices):
        if prices is None or len(prices)==0: return 0
        
        memo = [0]*len(prices)
        min_price = float('inf')
        
        for i in xrange(len(prices)):
            min_price = min(min_price, prices[i])
            if i==0: continue
            memo[i] = max(prices[i]-min_price, memo[i-1])
        return memo[-1]
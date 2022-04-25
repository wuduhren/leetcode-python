class Solution(object):
    def maxProfit(self, prices):
        if not prices or len(prices)<=1: return 0
        N = len(prices)

        buy = [-prices[0], max(-prices[1], -prices[0])]
        sell = [0, max(prices[1]+buy[0], 0)]
        
        for i in xrange(2, N):
            buy.append(max(sell[i-2]-prices[i], buy[i-1]))
            sell.append(max(prices[i]+buy[i-1], sell[i-1]))
            
        return max(buy[-1], sell[-1], 0)

"""
Three rules:
1. Need to buy before sell.
2. After sell, next day need to rest (cannot buy).
3. When buying, we spend money, which is a negative profit.

There are two possible end state. buy or sell. So we need to consider both.
Only considering prices 0~i, buy[i] stores the max profit that the last action is "buy".
Only considering prices 0~i, sell[i] stores the max profit that the last action is "sell".

Let's sort this out.
When i==0:
buy: -prices[0]
sell: 0, since we cannot sell at i==0.

When i==1:
buy: max(-prices[1], -prices[0])
Now, we must not have sell yet. So no need to consider it.
If we buy at i==1, the profit will be `-prices[1]`. But we also had the option not to buy. buy[0] is the max profit if we don't buy at i==1.
Again, we are considering, when the end state is "buy", what is the max profit?
Thus, `max(-prices[1], buy[0])`.

sell: max(prices[1]+buy[0], 0)
If we sell at i==1, the profit will be `prices[1]+buy[0]`. But we also had the option not to sell. 0 is the max profit if we don't sell at i==1.
Again, we are considering, when the end state is "sell", what is the max profit?
Thus, `max(prices[1]+buy[0], sell[0])`

When i>=2:




"""
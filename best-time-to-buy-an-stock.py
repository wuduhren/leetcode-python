#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution(object):
    def maxProfit(self, prices):
        if (len(prices)==0):
            return 0
        
        minPrice = prices[0]
        maxProfit = 0
        for price in prices:
            if (price<minPrice):
                minPrice = price
            if (price-minPrice>maxProfit):
                maxProfit = price-minPrice
        return maxProfit
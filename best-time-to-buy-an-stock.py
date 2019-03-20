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

"""
I really take time to make the best solution, because I wanted to help people understand.
If you like my answer, a star on GitHub I will really appreciated.
https://github.com/wuduhren/leetcode-python
"""
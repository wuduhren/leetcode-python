class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        ans = 0
        
        for i in range(1, len(prices)):
            ans = max(ans, prices[i]-minPrice)
            minPrice = min(prices[i], minPrice)
        
        return ans
"""
Bellman-Ford.
Time: O(KE)
"""
class Solution:
    def findCheapestPrice(self, N: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        prices = {n:float('inf') for n in range(N)}
        prices[src] = 0
        
        for k in range(K+1):
            temp = prices.copy()
            for source, destination, price in flights:
                if prices[source]==float('inf'): continue
                if prices[source]+price<temp[destination]:
                    temp[destination] = prices[source]+price
            prices = temp
        return prices[dst] if prices[dst]!=float('inf') else -1
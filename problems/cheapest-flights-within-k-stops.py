import heapq
import collections

"""
We start from src and only got K+1 stops to use
Each time, we choose the cheapest place to go.

If the city we popout is dst, then the price must be lowest
Since we always pick the lowest place to go.

If we still have stops left (stops>1), we put its neighbor to the priority queue.
So the city in the priority queue must be within the stops limit.

Making the graph takes O(E)
The size of priority queue is O(V), since we might put all the cities in it.
So for every pop, it is O(LogV). Total is O(VLogV).
For every edge we call an heappush, so that is ELogV
O(E+ (V+E)LogV) -> O((V+E)LogV)
V is the number of cities within range K stops.
"""
#Dijkstra
class Solution1(object):
	def findCheapestPrice(self, n, flights, src, dst, K):
		graph = collections.defaultdict(list)
		pq = []

		for u, v, w in flights: graph[u].append((w, v))

		heapq.heappush(pq, (0, K+1, src))
		while pq:
			price, stops, city = heapq.heappop(pq)

			if city is dst: return price
			if stops>0:
				for price_to_nei, nei in graph[city]:
					heapq.heappush(pq, (price+price_to_nei, stops-1, nei))
		return -1

"""
This is mostly straight forward BFS.
When we are out of stops, or price is greater than min_price, we stop adding cities to the queue.
Every time we encounter dst we compare the price and set it to the min.

Making the graph takes O(E)
BFS every node in adjacent list takes O(V+E)
V is the number of cities within range K stops.
"""
#BFS
class Solution2(object):
	def findCheapestPrice(self, n, flights, src, dst, K):
		graph = collections.defaultdict(list)
		q = collections.deque()
		min_price = float('inf')

		for u, v, w in flights: graph[u].append((w, v))
		q.append((src, 0, 0))
		while q:
			city, stops, price = q.popleft()
			if city==dst:
				min_price = min(min_price, price)
				continue

			if stops<=K and price<=min_price:
				for price_to_nei, nei in graph[city]:
					q.append((nei, stops+1, price+price_to_nei))

		return min_price if min_price!=float('inf') else -1


"""
Standard Dijkstra, except this time instead of only explore the ones with least price
We also need to explore the ones with less steps. So add stepFromSrc to check.

Time: O(ELogE), since there will be at most E edges that get pushed into the heap.
Space: O(E)
"""
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        priceFromSrc = {}
        stepFromSrc = {}
        h = [(0, 0, src)]
        G = collections.defaultdict(list)
        
        #build graph
        for s, d, p in flights:
            G[s].append((d, p))
        
        #dijkstra
        while h:
            price, k, node = heapq.heappop(h)
            
            if node==dst: return price
            if k>K: continue
            
            for nei, price2 in G[node]:
				#explore next destination with less price or less steps
                if nei not in priceFromSrc or price+price2<=priceFromSrc[nei] or k<stepFromSrc[nei]:
                    priceFromSrc[nei] = price+price2
                    stepFromSrc[nei] = k
                    heapq.heappush(h, (price+price2, k+1, nei))
                    
        return -1
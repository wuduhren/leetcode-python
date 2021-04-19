import bisect
class Solution(object):
    def lastStoneWeight(self, stones):
        stones.sort()
        
        while len(stones)>1:
            x = stones.pop()
            y = stones.pop()
            bisect.insort_left(stones, abs(x-y))

        return 0 if not stones else stones[0]

import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        h = []
        
        for stone in stones:
            heapq.heappush(h, stone*-1)
        
        while len(h)>1:
            x = heapq.heappop(h)
            y = heapq.heappop(h)
            heapq.heappush(h, abs(x-y)*-1)
        
        return 0 if not h else abs(h[0])
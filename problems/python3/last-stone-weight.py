class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones)>=2:
            w1 = -heapq.heappop(stones)
            w2 = -heapq.heappop(stones)
            
            if w1-w2>0: heapq.heappush(stones, -(w1-w2))
        
        return -stones[0] if stones else 0
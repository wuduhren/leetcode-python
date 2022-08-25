class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        
        for x, y in points:
            dis = (x**2+y**2)**0.5
            heapq.heappush(h, (-dis, x, y))
            if len(h)>k: heapq.heappop(h)
        
        return [(x, y) for dis, x, y in h]
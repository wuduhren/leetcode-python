class Solution(object):
    def kClosest(self, points, k):
        h = []
        
        for x, y in points:
            d = (x**2+y**2)**0.5
            if len(h)>=k and -h[0][0]>d:
                heapq.heappop(h)
                heapq.heappush(h, (-d, x, y))
            elif len(h)>=k and -h[0][0]<=d:
                pass
            else:
                heapq.heappush(h, (-d, x, y))
        
        return [(x, y) for _, x, y in h]
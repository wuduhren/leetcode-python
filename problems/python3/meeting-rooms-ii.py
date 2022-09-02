class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        h = []
        ans = 0
        
        for s, e in intervals:
            while h and s>=h[0][0]:
                heapq.heappop(h)
            heapq.heappush(h, (e, s))
            ans = max(ans, len(h))
        return ans
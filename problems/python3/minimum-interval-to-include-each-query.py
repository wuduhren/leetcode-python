class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ans = [-1]*len(queries)
        queries = sorted([(query, i) for i, query in enumerate(queries)])
        intervals.sort()
        h = []
        
        itervalIndex = 0
        for query, queryIndex in queries:
            #push all intervals that include 'query' to the min heap
            while itervalIndex<len(intervals) and intervals[itervalIndex][0]<=query:
                left = intervals[itervalIndex][0]
                right = intervals[itervalIndex][1]
                size = right-left+1
                heapq.heappush(h, (size, right))
                itervalIndex += 1
            
            #pop all intervals that not includes 'query' out of the min heap
            while h and h[0][1]<query:
                heapq.heappop(h)
                
            if h: ans[queryIndex] = h[0][0]
        return ans
"""
Time: O(NLogN) for sorting.
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        ans = 0
        prevEnd = intervals[0][1]
        
        for s, e in intervals[1:]:
            if s>=prevEnd:
                prevEnd = e
            else:
                ans += 1
                prevEnd = min(prevEnd, e)
        return ans
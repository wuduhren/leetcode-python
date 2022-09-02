"""
Time: O(NLogN) for sorting
Space: O(1) excluding the output.
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        
        for s, e in intervals:
            if not ans:
                ans.append([s, e])
            elif ans[-1][1]>=s:
                ans[-1][1] = max(ans[-1][1], e)
            else:
                ans.append([s, e])
        return ans
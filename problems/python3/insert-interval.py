class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        
        #add intervals before newInterval
        while i<len(intervals) and intervals[i][1]<newInterval[0]:
            ans.append(intervals[i])
            i += 1
        
        #add newInterval and merge the overlapped
        ans.append(newInterval)
        while i<len(intervals) and intervals[i][0]<=ans[-1][1]:
            ans[-1][0] = min(ans[-1][0], intervals[i][0])
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
            i += 1
        
        #add intervals after newInterval
        while i<len(intervals):
            ans.append(intervals[i])
            i += 1
            
        return ans
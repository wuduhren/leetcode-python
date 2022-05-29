class Solution(object):
    def insert(self, intervals, newInterval):
        if not intervals: return [newInterval]
        
        max_index = float('-inf')
        min_index = float('inf')
        s0 = newInterval[0]
        e0 = newInterval[1]
        
        for i, interval in enumerate(intervals):
            s = interval[0]
            e = interval[1]
            
            if not (newInterval[1]<s or e<newInterval[0]):
                s0 = min(s0, s)
                e0 = max(e0, e)
                max_index = max(max_index, i)
                min_index = min(min_index, i)
       
        return intervals[:min_index]+[[s0, e0]]+intervals[max_index+1:] if min_index!=float('inf') else sorted(intervals+[[s0, e0]])
"""
imagine a number line, we put all the numbers on it and draw a line between two numbers for each interval.
for all the overlap lines we just want the start and the end

we need to sort the array of intervals, so we won't miss any overlaps by iterate through the array once. [1]

first we check if there is overlaps
if we the end of the last interval is greater or equal than the start of this inteval, we found the overlaps. [2]
so we need to update the last interval's end [3]

if there is no overlaps [4]
we don't need to do anything, just put it in the array 
"""
class Solution(object):
    def merge(self, intervals):
        result = []
        intervals.sort() #[1]
        
        for inter in intervals:
            if len(result)>0 and result[-1][1]>=inter[0]: #[2]
                result[-1][1] = max(result[-1][1], inter[1]) #[3]
            else: #[4]
                result.append(inter) 
        return result
        

class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        
        i = 0
        while i<len(intervals)-1:
            if intervals[i][1]>=intervals[i+1][0]:
                intervals = intervals[:i] + [[min(intervals[i][0], intervals[i+1][0]), max(intervals[i][1], intervals[i+1][1])]] + intervals[i+2:]
            else:
                i += 1
        return intervals
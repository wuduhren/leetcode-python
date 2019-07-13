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
        intervals.sort(key=lambda x: x.start) #[1]
        
        for inter in intervals:
            if len(result)>0 and result[-1].end>=inter.start: #[2]
                result[-1].end = max(result[-1].end, inter.end) #[3]
            else: #[4]
                result.append(inter) 
        return result
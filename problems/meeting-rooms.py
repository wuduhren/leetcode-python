"""
Time: O(NLogN)
Space: O(1)

Sort the interval (mainly by start time), see if the end overlaps with the start of next.
"""
class Solution(object):
    def canAttendMeetings(self, intervals):
        intervals.sort()
        
        for i in xrange(len(intervals)-1):
            end = intervals[i][1]
            nextStart = intervals[i+1][0]
            if end>nextStart: return False
        
        return True
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        lastEnd = float('-inf')
        for s, e in intervals:
            if lastEnd>s:
                return False
            else:
                lastEnd = e
        return True
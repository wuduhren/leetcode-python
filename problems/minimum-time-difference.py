"""
Time: O(1440)
Space: O(1440)
"""
class Solution(object):
    def findMinDifference(self, timeStrings):
        def timeStringToMinutes(timeString):
            time = timeString.split(':')
            h = int(time[0])
            m = int(time[1])
            return h*60+m
        
        ans = float('inf')
        minTime = float('inf')
        maxTime = float('-inf')
        timeSet = set()
        for timeString in timeStrings:
            t = timeStringToMinutes(timeString)
            if t in timeSet: return 0
            minTime = min(minTime, t)
            maxTime = max(maxTime, t)
            timeSet.add(t)
        
        
        prev = None
        for t in xrange(minTime, maxTime+1):
            if t not in timeSet: continue
            if prev!=None: ans = min(ans, t-prev)
            prev = t
        
        ans = min(ans, 1440+minTime-maxTime) #compare minTime and maxTime
        return ans
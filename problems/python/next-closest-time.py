"""
Time: O(1), since we at most iterate 24 times for hour and 60 times for minutes.
Space: O(1).

The main idea is to check if we can change the minute only.
If not, we get the next hour with the smallest minute.
"""
class Solution(object):
    def nextClosestTime(self, time):
        def getNextHour():
            currentHour = int(time[0]+time[1]) if time[0]!='0' else int(time[1])
            
            for h in xrange(currentHour+1, 24):
                hs = str(h) if h>9 else '0'+str(h)
                if all([c in digits for c in hs]): return hs
            return ''
        
        def getSmallestHour():
            for h in xrange(0, 24):
                hs = str(h) if h>9 else '0'+str(h)
                if all([c in digits for c in hs]): return hs
            return ''
        
        def getNextMinute():
            currentMinute = int(time[3]+time[4]) if time[3]!='0' else int(time[4])
            
            for m in xrange(currentMinute+1, 60):
                ms = str(m) if m>9 else '0'+str(m)
                if all([c in digits for c in ms]): return ms
            return ''
        
        def getSmallestMinute():
            for m in xrange(0, 60):
                ms = str(m) if m>9 else '0'+str(m)
                if all([c in digits for c in ms]): return ms
            return ''
                
        digits = set([time[0], time[1], time[3], time[4]])
        nextMinute = getNextMinute()
        if nextMinute:
            return time[:3]+nextMinute
        else:
            return (getNextHour() or getSmallestHour())+':'+getSmallestMinute()
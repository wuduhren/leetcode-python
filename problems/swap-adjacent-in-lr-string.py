class Solution(object):
    def canTransform(self, start, end):
        if len(start)!=len(end): return False
        if start.replace('X', '')!=end.replace('X', ''): return False
        
        startLIndex = [i for i, c in enumerate(start) if c=='L']
        endLIndex = [i for i, c in enumerate(end) if c=='L']
        for i in xrange(len(startLIndex)):
            if startLIndex[i]<endLIndex[i]:
                return False
        
        startRIndex = [i for i, c in enumerate(start) if c=='R']
        endRIndex = [i for i, c in enumerate(end) if c=='R']
        for i in xrange(len(startRIndex)):
            if startRIndex[i]>endRIndex[i]:
                return False
        
        return True
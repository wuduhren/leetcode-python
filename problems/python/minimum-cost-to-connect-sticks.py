class Solution(object):
    def connectSticks(self, sticks):
        if not sticks or len(sticks)==1: return 0
        h = []
        
        for n in sticks:
            heapq.heappush(h, n)
        
        cost = 0
        while len(h)>1:
            currSum = heapq.heappop(h)+heapq.heappop(h)
            cost += currSum
            heapq.heappush(h, currSum)
        
        return cost
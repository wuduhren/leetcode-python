class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k):
            timeNeeded = 0
            for pile in piles:
                timeNeeded += math.ceil(pile/k)
            return timeNeeded<=h
        
        kMin = 1
        kMax = max(piles)
        ans = kMax
        
        while kMin<=kMax:
            k = kMin + int((kMax-kMin)/2)
            if canFinish(k):
                ans = min(ans, k)
                kMax = k-1
            else:
                kMin = k+1
        
        return ans
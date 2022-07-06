class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0: return False
        
        counter = collections.Counter(hand)
        h = list(counter.keys())
        heapq.heapify(h)
        
        while h:
            minNum = h[0]
            for n in range(minNum, minNum+groupSize):
                if counter[n]<=0: return False
                counter[n] -= 1
                if counter[n]==0:
                    if h[0]!=n: return False
                    heapq.heappop(h)
        
        return True
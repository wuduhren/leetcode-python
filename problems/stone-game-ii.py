class Solution(object):
    def stoneGameII(self, piles):
        def helper(start, m):
            if (start, m) in history: return history[(start, m)]
            
            if start>=len(piles): return 0
            if start+m*2>=len(piles): return sum(piles[start:])
            
            stones = float('-inf')
            for x in xrange(1, m*2+1):
                stones = max(stones, sum(piles[start:])-helper(start+x, max(m, x)))
            
            history[(start, m)] = stones
            return history[(start, m)]
        
        history = {}
        return helper(0, 1)
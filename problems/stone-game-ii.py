class Solution(object):
    def stoneGameII(self, piles):
        def helper(start, m):
            if (start, m) in history: return history[(start, m)]
            
            if start>=len(piles): return 0
            if start+m*2>=len(piles): return sum(piles[start:])
            
            max_stones = float('-inf')
            for x in xrange(1, m*2+1):
                max_stones = max(max_stones, sum(piles[start:])-helper(start+x, max(m, x)))
            
            history[(start, m)] = max_stones
            return history[(start, m)]
        
        history = {}
        return helper(0, 1)

"""
helper(start, m) := the max stones that the first player will get with given piles[start:] and M.
max_stones = MAX{ (sum of all the stones) - (max_stones the other player will get) } = MAX{ sum(piles[start:]) - helper(start+x, max(m, x)) }
"""
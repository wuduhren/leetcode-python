class Solution(object):
    def shipWithinDays(self, weights, D):
        l = max(weights)
        r = sum(weights)
        
        while l<r:
            c = (l+r)/2
            
            #calculate with weight capacity c, how many days we need, d.
            d = 0
            daily_weight = 0
            for w in weights:
                if daily_weight+w<=c:
                    daily_weight+=w
                else:
                    daily_weight = w
                    d += 1
            if daily_weight: d += 1

            if d>D:
                #K cannot be the answer.
                #next round we don't need to put K in l~r.
                l = c+1
            else:
                #K might ot might not be the answer.
                #next round we still need to put K in l~r.
                r = c
        return l

"""
This is a binary search problem.
If you do not understand binary search yet, please study it first.

[0]
Lets define the possible range, `l` and `r`, of our answer, the least weight capacity of the ship that can diliver all packages within D days.
The ship must at least carry the heaviest package, so `l = max(weights)`.
The best ship scenario is that we can carry all packages at once, so `r = sum(weights)`.

[1]
For every iteration, we try a `c` (capacity) and adjust `l` and `r`.
Note that, even if `d<=D`, we still need to see if there are any smaller `d`.

[2]
So the boundary of our answer, `l` and `r`, will collides together (`l==r`) and jump out of the loop.

Time complexity: `O(NlogN)`. There will be `O(LogN)` iteration. For every iteration we need O(N) to calculate the `t`. `N` is the length of `piles`.
Space complexity is O(N). For calculating `t`.
"""
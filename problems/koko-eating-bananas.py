"""
`l` is the minimum possible ans.
`h` is the lowest value that we are sure that koko is able to finish all.
Since koko have to rest for the entire K even if he finish that pile already.
The H cannot be lowwer than `len(piles)`.
So we are sure that koko is able to finish all the piles in `max(piles)` of speed.

Now, we need to make logical guess between `l` and `h` by binary search.
If `m` (`(l+h)/2`) is able to finish all the piles in `H`, we lowwer the `h` to `m`.
If `m` is not able to finish, we raise the `l` to `m+1`.
We keep on adjust `l` and `r` until `l` is equal to `r`.
"""
class Solution(object):
    def minEatingSpeed(self, piles, H):
        def canEatAll(time):
            return sum((p+time-1)/time for p in piles) <= H
            # time_required = 0
            # for count in piles:
            #     time_required += math.ceil(count/float(time))
            # return time_required<=H

        l = 1
        h = max(piles)

        while l<h:
            m = (l+h)/2
            if canEatAll(m):
                h = m
            else:
                l = m+1
        return l

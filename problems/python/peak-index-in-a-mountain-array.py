"""
Take a look at the code first.
If `A[p]<A[p+1]`, it means the `p` and `p+1` is at the left side of the mountain,
We move `l` to `p+1`, since the peak must be at `p+1` or the right of the `p+1`.
Else, it means the `p` and `p+1` is at the right side of the mountain,
We move the `r` to `p`, since the peak must be at `p` or the left of the `p`.
The `l` and `r` will move closer and closer to the peak until they meet together.
The time complexity is `O(LogN)`
"""
class Solution(object):
    def peakIndexInMountainArray(self, A):
        l = 0
        r = len(A)-1
        while l<r:
            p = (l+r)/2
            if A[p]<A[p+1]:
                l = p+1
            else:
                r = p
        return l

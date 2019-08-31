"""
The ans must be in between 0 and `x`.
So we set the lower bound `l` to 0. The upper bound `r` to `x`.
The answer will always between `l` and `r`.
For every iteration, if `l`, `m`, `r` are not answer, we adjust the `l` or `r`.
Until we find the answer
"""
class Solution(object):
    def mySqrt(self, x):
        def isAns(a):
            if a**2<=x and (a+1)**2>x:
                return True
            return False

        l = 0
        r = x
        while True:
            m = (l+r)/2
            if isAns(l): return l
            if isAns(m): return m
            if isAns(r): return r

            if m**2<x:
                l = m+1
            else:
                r = m-1
        return -1

"""
Time: O(LogN)
Space: O(1)

Since citations is sorted,
i = N-1, if 1<=citations[i], it means that at least 1 of the citations is larger than 1. h-index is 1.
i = N-2, if 2<=citations[i], it means that at least 2 of the citations is larger than 2. h-index is 2.
...
i = 0, if N<=citations[i], it means that at least N of the citations is larger than N. h-index is N.

We can iterate from N-1 to 0. See what h-index ends up. Using O(N) of time.

We can also binary search the i, see which i match the condition.
"""
class Solution(object):
    def hIndex(self, citations):
        N = len(citations)
        
        l = 0
        r = N-1
        
        while l<r:
            i = (l+r)/2
            h = N-i

            if citations[i]>=h:
                #h may be the h-index, check larger h.
                r = i
            else:
                #h is not h-index, check smaller h.
                l = i+1
        
        #now, l is equal to r

        return N-l if citations[l]!=0 else 0  #take care of edge case [0], [0, 0] or [0, 0, 0]
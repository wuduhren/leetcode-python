"""
Let's look at the naive approach first.

Each day we turn on a bulb by `bulbs[i] = 1` and
1. `check()` the bulb on i to i+(K+1), see if it matches the pattern 1,0,0,..1
2. `check()` the bulb on i to i-(K+1), see if it matches the pattern 1,0,0,..1
The `check()` will take O(K), so the time complexity will be O(NK), N is the number of bulbs.

Since iterating the bulbs seems inevitable, the only thing we can avoid is the iteration between l and r in `check()` which is taking O(K) of time.
"""
class Solution(object):
    def kEmptySlots(self, schedule, K):
        def check(l, r):
            if l<0 or r>=len(bulbs): return False
            if bulbs[l]!=1 or bulbs[r]!=1: return False
            for k in xrange(l+1, r):
                if bulbs[k]!=0: return False
            return True
        
        bulbs = [0]*len(schedule)
        for day, x in enumerate(schedule):
            i = x-1
            bulbs[i] = 1
            if check(i, i+K+1): return day+1
            if check(i-(K+1), i): return day+1
        return -1


"""
The reason we iterate between l and r is because we need to check there are only "0" between l and r, no "1".
This is where we can use SortedSet (also known as TreeSet in Java).
For each day, we also add "1" index to the SortedSet.
So instead of checking if it is all "0" between l and r, we check if there is any "1" between l and r.

i = ss.bisect_right(l). The insetion point to a sorted list. If exist the same, insert to the right.
j = ss.bisect_left(r). The insetion point to a sorted list. If exist the same, insert to the left.

j==0 means that r is the smallest index in the SortedSet.
i==len(ss) means that l is the largest index in the SortedSet.
i==j means that there is no other "1" between l and r.

The time complexity is will be O(NLogN)
"""
from sortedcontainers import SortedSet

class Solution(object):
    def kEmptySlots(self, schedule, K):
        def check(l, r):
            if l<0 or r>=len(bulbs): return False
            if bulbs[l]!=1 or bulbs[r]!=1: return False
            
            i = ss.bisect_right(l)
            j = ss.bisect_left(r)
            
            return j!=0 and i!=len(ss) and i==j
        
        bulbs = [0]*len(schedule)
        ss = SortedSet()
        for day, x in enumerate(schedule):
            i = x-1
            bulbs[i] = 1
            ss.add(i)
            if check(i, i+K+1): return day+1
            if check(i-(K+1), i): return day+1
        return -1
import collections
import bisect

class TimeMap(object):

    def __init__(self):
        self.t = collections.defaultdict(list)
        self.v = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.t[key].append(timestamp)
        self.v[key].append(value)

    def get(self, key, timestamp):
        if len(self.t[key])==0: return ""
        i = bisect.bisect(self.t[key], timestamp)
        return self.v[key][i-1] if i>0 else ""


import collections

class TimeMap(object):
    def __init__(self):
        self.t = collections.defaultdict(list)
        self.v = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.t[key].append(timestamp)
        self.v[key].append(value)

    def get(self, key, timestamp):
        if len(self.t[key])==0: return ""
        i = self.bisect(self.t[key], timestamp)
        return self.v[key][i-1] if i>0 else ""

    def bisect(self, A, x):
        if A is None or len(A)==0: return 0

        l = 0
        r = len(A)-1
        while l<=r:
            if x<A[l]: return l
            elif A[l]==x: return l+1
            elif A[r]<=x: return r+1

            p = (l+r)/2
            if x<A[p]:
                r = p-1
            elif A[p]==x:
                return p+1
            else:
                l = p+1
        return l

"""
We need a hash-table to store the key-value information.
For every key, there are multiple values and we need it to sort by`timestamp`.

First, we use two array, `t` and `v` to store timestamp and value separately.
And becuase the problem says **The timestamps for all TimeMap.set operations are strictly increasing.**
So for the `set()` method, we only need to simply append `value` and `timestamp` to the end of `v` and `t`.
The array `t` and its corresponding `v` is sorted already.

[bisect](https://docs.python.org/2/library/bisect.html) can help us implement our `get()` method.
It returns an insertion point which comes after (to the right of) any existing entries, if we insert the **`timestamp` we are going to get()** into a the array, `t`.
So `bisect(t, timestamp)` returns `i`:
    * If `i==0`: it means that there are no value samller than the `timestamp`, `return ""`.
    * If `i>0`: it means `i` is the index where its value just exceed the `timestamp`, return the value at `i-1`.

We can also implement our own `bisect` by binary search.
The implementation assume there are no duplicate value in the array.

Time Complexity, O(1) for `set()`. O(LogN) for `get()`.
Space complexity is O(N)
N is the number of value stored.
"""

t = TimeMap()
t.set('love', 'low', 10)
t.set('love', 'high', 20)
print t.get('love', 5)
print t.get('love', 10)
print t.get('love', 15)
print t.get('love', 20)
print t.get('love', 25)



#2020/7/20
from collections import defaultdict
class TimeMap(object):

    def __init__(self):
        self.v = defaultdict(list)
        self.t = defaultdict(list)
        

    def set(self, key, value, timestamp):
        self.v[key].append(value)
        self.t[key].append(timestamp)
        

    def get(self, key, timestamp):
        if key not in self.t: return ""
        i = self.bisect(self.t[key], timestamp)
        return self.v[key][i-1] if i>0 else ""
    

    #return an insertion point right to an index
    #where the target's value just exceed the index's value
    def bisect(self, L, target): 
        if not L: return 0

        l = 0
        r = len(L)-1

        while l<=r:
            if target<L[l]: return l
            if target==L[l]: return l+1
            if target>=L[r]: return r+1
            
            m = (l+r)/2

            if target==L[m]:
                return m+1
            elif target<L[m]:
                r = m-1
            else:
                l = m+1
        return 0
"""
Time Complexity: set(), O(1). get(), O(LogN).
Space Complexity: O(N).
"""

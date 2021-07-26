"""
Time: O(LogN)
Space: O(1)

This problem is very similar to problem 374.

`l` is the lower bound of the possible versions.
`h` is the higher bound of the possible versions.
We always guess the version in the middle of `l` and `h`, which is `v`.
If v is bad version and v-1 is not, we found the answer. Return `v`.
If v and v-1 are both good version, we know that the answer will be larger than v, so the lower bound (`l`) is now v+1.
If v and v-1 are both bad version, we know that the answer is smaller than v, so the higher bound (`h`) is now v-1.
"""
class Solution(object):
    def firstBadVersion(self, n):
        if isBadVersion(1): return 1
        
        l = 2
        h = n
        
        while l<h:
            v = (l+h)/2
            r1 = isBadVersion(v)
            r2 = isBadVersion(v-1)
            
            if r1 and not r2:
                return v
            elif not r1 and not r2:
                l = v+1
            elif r1 and r2:
                h = v-1
                
        return (l+h)/2
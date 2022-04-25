import collections

class Solution(object):
    def deleteAndEarn(self, nums):
        if not nums: return 0
        m = min(nums)
        M = max(nums)
        c = collections.Counter(nums)
        
        prev = 0 
        curr = 0
        for n in xrange(m, M+1):
            prev, curr = curr, max(prev+n*c[n], curr)
        return curr
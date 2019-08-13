"""
Take a look at the code first.
If `nums[p]<nums[p+1]`, it means the `p` and `p+1` is at the left side of the mountain,
We move `l` to `p+1`, since the peak must be at `p+1` or the right of the `p+1`.
Else, it means the `p` and `p+1` is at the right side of the mountain,
We move the `r` to `p`, since the peak must be at `p` or the left of the `p`.
The `l` and `r` will move closer and closer to the peak until they meet together.
The time complexity is O(LogN)
"""
class Solution(object):
    def findPeakElement(self, nums):
        l = 0
        r = len(nums)-1
        while l<r:
            p = (l+r)/2
            if nums[p]<nums[p+1]:
                l = p+1
            else:
                r = p
        return l


#O(N) Solution
class Solution(object):
    def findPeakElement(self, nums):
        if nums is None or len(nums)==0: return None
        for i in xrange(len(nums)):
            l = nums[i-1] if (i-1)>=0 else float('-inf')
            r = nums[i+1] if (i+1)<len(nums) else float('-inf')
            if nums[i]>l and nums[i]>r: return i
        return None

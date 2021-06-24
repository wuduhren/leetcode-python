"""
As we move right the i and increament s, if the s >= target, we 

"""
class Solution(object):
    def minSubArrayLen(self, target, nums):
        s = 0
        l = 0
        ans = float('inf')
        
        for i in xrange(len(nums)):
            s += nums[i]
            
            while s>=target:
                ans = min(i-l+1, ans)
                s -= nums[l]
                l += 1
        
        return ans if ans!=float('inf') else 0
                
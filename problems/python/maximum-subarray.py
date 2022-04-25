#https://leetcode.com/problems/maximum-subarray/
"""
[0]
if we know the max value of the subarray that ends at i index is Mi
what is the max value of the subarray that ends at i+1 index?
its either nums[i+1] or nums[i+1]+Mi
so code below, maxCurrent[i] stores the max value of subarray that ends at i

[1]
the max value of the subarray that ends at 0, has to be nums[0].

[2]
the max value of subarray must ends in one of the index of nums
so we get the max(maxCurrent).
"""
class Solution(object):
    def maxSubArray(self, nums):
        if nums==None or len(nums)==0: return None
        maxCurrent = [nums[0]] #[1]
        for i in xrange(1, len(nums)):
            maxCurrent.append(max(nums[i], nums[i]+maxCurrent[-1])) #[0]
        return max(maxCurrent) #[2]

# 2020/11/14
class Solution(object):
    def maxSubArray(self, nums):
        ans = nums[0]
        last_max = nums[0]
        
        for i in xrange(len(nums)):
            if i==0: continue
            last_max = max(nums[i], nums[i]+last_max)
            ans = max(ans, last_max)
            
        return ans
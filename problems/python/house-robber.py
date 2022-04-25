"""
For every index i in K
i is the max value we can rob when we only consider 0~i, so
if i is 0, the max value is nums[0] because there are only nums[0]
if i is 1, the max value is max(nums[0], nums[1]), since we only consider 0~1
if i is 2~the end, the max value depends on whether the previous one is selected, because we cannot rob two continuos house
* if the previous one (i-1) is selected, then the max value is either #[1]
    * we not select i-1 and select this house (K[i] = K[i-2]+nums[i]), or
    * we simply don't select this house, if we don't select this house the value will be the same as i-1 (K[i] = K[i-1])
* if the previouse one is not selected, we simply rob this house #[2]

Time Complexity is simply O(N), N is the number of houses.
"""
class Solution(object):
    def rob(self, nums):
        if (len(nums)==0): return 0
        K = [0]*len(nums)
        for i in xrange(len(nums)):
        	if i==0:
        		K[i] = nums[0]
        	elif i==1:
        		K[i] = max(nums[0], nums[1])
        	else:
        		prev_selected = K[i-1]!=K[i-2] 
        		if prev_selected: #[1]
        			K[i] = max(K[i-2]+nums[i], K[i-1])
        		else: #[2]
        			K[i] = K[i-1]+nums[i]
        return K[-1]

#2020/11/14
class Solution(object):
    def rob(self, nums):
        def helper(i):
            if i>=len(nums): return 0
            if i in history: return history[i]
            history[i] = max(nums[i]+helper(i+2), helper(i+1))
            return history[i]
        
        history = {}
        return helper(0)

#2020/11/14
class Solution(object):
    def rob(self, nums):
        if not nums: return 0
        if len(nums)==0 or len(nums)==1: return max(nums)
        
        last1 = max(nums[0], nums[1])
        last2 = nums[0]
        
        for i in xrange(len(nums)):
            if i==0 or i==1: continue
            last2, last1 = last1, max(nums[i]+last2, last1)
            
        return last1
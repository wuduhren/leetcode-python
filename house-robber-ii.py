"""
See [House robber](https://leetcode.com/problems/house-robber) first and with my [explaination](https://leetcode.com/problems/house-robber/discuss/321383).
They are essentially the same, except for the fact that the first and the last house is connected.
So we have to take into consideration that whether the first and the last is connected.
The scenario can break into two: **Either the first house get robbed or not.**
"""
class Solution(object):
    def rob(self, nums):
        if (len(nums)==0): return 0

        #first robbed
        K = [0]*len(nums)
        for i in xrange(len(nums)):
        	if i==0:
        		K[i] = nums[0]
        	elif i==1:
        		K[i] = max(nums[0], nums[1])
        	elif i==len(nums)-1:
        		K[i] = K[i-1]
        	else:
        		prev_selected = K[i-1]!=K[i-2] 
        		if prev_selected:
        			K[i] = max(K[i-2]+nums[i], K[i-1])
        		else:
        			K[i] = K[i-1]+nums[i]
        v1 = K[-1]

        #first not robbed
        K = [0]*len(nums)
        for i in xrange(len(nums)):
        	if i==0:
        		K[i] = 0
        	elif i==1:
        		K[i] = nums[1]
        	else:
        		prev_selected = K[i-1]!=K[i-2] 
        		if prev_selected:
        			K[i] = max(K[i-2]+nums[i], K[i-1])
        		else:
        			K[i] = K[i-1]+nums[i]
        v2 = K[-1]
        return max(v1, v2)
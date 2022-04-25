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
        		K[i] = nums[0]
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

#2020/11/15
class Solution(object):
    def rob(self, nums):
        if not nums: return 0
        if len(nums)==0 or len(nums)==1: return max(nums)
        N = len(nums)
        
        v1 = nums[0]
        v2 = nums[0]
        for i in xrange(2, N-1):
            v1, v2 = max(nums[i]+v2, v1), v1
        
        w1 = nums[1]
        w2 = 0
        for i in xrange(2, N):
            w1, w2 = max(nums[i]+w2, w1), w1
        
        return max(v1, w1)
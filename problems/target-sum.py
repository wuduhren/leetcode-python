class Solution(object):
    def findTargetSumWays(self, nums, S):
        stack = [(0, 0)]
        ans = 0
        
        while stack:
            i, s = stack.pop()
            if i==len(nums) and s==S: ans += 1
            if i>=len(nums): continue
            
            stack.append((i+1, s+nums[i]))
            stack.append((i+1, s-nums[i]))
        
        return ans

import collections



class Solution(object):
    def findTargetSumWays(self, nums, target):
        S = sum(nums)
        dp = [collections.Counter() for _ in xrange(len(nums)+1)]
        dp[0][0] = 1
        
        for i in xrange(1, len(nums)+1):
            for j in xrange(-S, S+1):
                dp[i][j] = dp[i-1][j+nums[i-1]] + dp[i-1][j-nums[i-1]]
        
        return dp[len(nums)][target]
        
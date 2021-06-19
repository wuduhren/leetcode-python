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

"""
dp[i][j] = number of ways to sum to j using nums[0~i-1]
Time: O(SN)
Space: O(SN)
"""


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


#2021/6/7
"""
dp[i][t] := number of ways nums[:i] can sum up to t applying + or -.
For all i, calculate all posible target (From minTarget~maxTarget)
"""
class Solution(object):
    def findTargetSumWays(self, nums, target):
        N = len(nums)
        maxTarget = sum(nums)
        minTarget = -maxTarget
        
        if target<minTarget or target>maxTarget: return 0
        
        dp = [[0 for _ in xrange(minTarget, maxTarget+1)] for _ in xrange(N+1)]
        
        dp[0][0] = 1
        
        for i in xrange(1, N+1):
            for t in xrange(minTarget, maxTarget+1):
                dp[i][t] = (dp[i-1][t-nums[i-1]] if t-nums[i-1]>=minTarget else 0) + (dp[i-1][t+nums[i-1]] if t+nums[i-1]<=maxTarget else 0)
        
        return dp[N][target]
class Solution(object):
    def combinationSum4(self, nums, target):
        def helper(t):
            if t<0: return 0
            if dp[t]>=0: return dp[t]
            
            ans = 0
            for num in nums:
                ans += helper(t-num)
            
            dp[t] = ans
            return ans
        
        dp = [-1]*(target+1)
        dp[0] = 1
        
        for i in xrange(target+1):
            helper(i)
        return dp[target]

"""
Time: O(TN), T is the value of target and N is the count of nums.
Space: O(T)
"""
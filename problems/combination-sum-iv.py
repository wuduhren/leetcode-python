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


"""
dp[n] := number of combs sums up to n

For example, lets say target is 32 and nums is [4,2,1].
dp[32] = dp[28]+dp[30]+dp[31]
Since the combs of dp[28] adds 4 will all equals to 32.
Since the combs of dp[30] adds 2 will all equals to 32.
Since the combs of dp[31] adds 1 will all equals to 32.

...

dp[28] = dp[24]+dp[26]+dp[27]
Since the combs of dp[28] adds 4 will all equals to 24.
Since the combs of dp[28] adds 2 will all equals to 26.
Since the combs of dp[28] adds 1 will all equals to 27.

...



Time: O(TN), T is the value of target and N is the count of nums.
Space: O(T)
"""
class Solution(object):
    def combinationSum4(self, nums, target):
        dp = [0]*(target+1)
        dp[0] = 1
        
        t = 1
        
        while t<=target:
            combs = 0
            for num in nums:
                if t-num<0: continue
                combs += dp[t-num]
            
            dp[t] = combs
            t += 1
            
        return dp[target]
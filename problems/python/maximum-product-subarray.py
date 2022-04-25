"""
Time: O(N)
Space: O(N)

dp[i][0] := the maximum subarray product that includes nums[i]
dp[i][1] := the minimum subarray product that includes nums[i]
"""
class Solution(object):
    def maxProduct(self, nums):
        if not nums: return 0
        dp = [[float('-inf'), float('inf')] for _ in xrange(len(nums))]
        
        dp[0] = [nums[0], nums[0]]
        ans = nums[0]
        
        for i in xrange(1, len(nums)):
            if nums[i]==0:
                dp[i][0] = 0
                dp[i][1] = 0
            elif nums[i]>0:
                dp[i][0] = dp[i-1][0]*nums[i] if dp[i-1][0]>0 else nums[i]
                dp[i][1] = dp[i-1][1]*nums[i] if dp[i-1][1]<=0 else nums[i]
            else:
                dp[i][0] = dp[i-1][1]*nums[i] if dp[i-1][1]<=0 else nums[i]
                dp[i][1] = dp[i-1][0]*nums[i] if dp[i-1][0]>0 else nums[i]
                
            ans = max(ans, dp[i][0])
            
        return ans

"""
The above solution can further reduce the space complexity to O(1).
"""
class Solution(object):
    def maxProduct(self, nums):
        if not nums: return 0
        
        maxLast = nums[0]
        minLast = nums[0]
        ans = nums[0]
        
        for i in xrange(1, len(nums)):
            if nums[i]==0:
                newMax = 0
                newMin = 0
            elif nums[i]>0:
                newMax = maxLast*nums[i] if maxLast>0 else nums[i]
                newMin = minLast*nums[i] if minLast<=0 else nums[i]
            else:
                newMax = minLast*nums[i] if minLast<=0 else nums[i]
                newMin = maxLast*nums[i] if maxLast>0 else nums[i]
            
            maxLast = newMax
            minLast = newMin
            ans = max(ans, maxLast)
            
        return ans
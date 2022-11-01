"""
Time: O(N)
Space: O(N), can be reduce to O(1)

dp[i][0] := The max product from subarray that end with nums[i]
dp[i][1] := The min product from subarray that end with nums[i]
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[1, 1] for _ in range(N+1)]
        ans = float('-inf')
        
        for i in range(1, N+1):
            dp[i][0] = dp[i][1] = nums[i-1]
            
            if nums[i-1]>0:
                dp[i][0] = max(dp[i][0], nums[i-1]*dp[i-1][0])
                dp[i][1] = min(dp[i][1], nums[i-1]*dp[i-1][1])
            else:
                dp[i][0] = max(dp[i][0], nums[i-1]*dp[i-1][1])
                dp[i][1] = min(dp[i][1], nums[i-1]*dp[i-1][0])
            ans = max(ans, dp[i][0])
        
        return ans
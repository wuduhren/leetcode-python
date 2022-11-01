"""
Time: O(N)
Space: O(N), can reduece to O(1).

dp[i][0] := max revenue if house i robbed
dp[i][1] := max revenue if house i not robbed
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[0, 0] for _ in range(N)]
        dp[0][0] = nums[0]
        
        for i in range(1, N):
            dp[i][0] = nums[i]+dp[i-1][1]
            dp[i][1] = max(dp[i-1])
        return max(dp[-1])
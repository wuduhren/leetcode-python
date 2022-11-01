class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=1: return max(nums)
        
        N = len(nums)
        dp = [[0, 0] for _ in range(N)]
        dp[0][0] = nums[0]
        
        for i in range(1, N):
            dp[i][0] = nums[i]+dp[i-1][1]
            dp[i][1] = max(dp[i-1])
        
        dp2 = [[0, 0] for _ in range(N)]
        for i in range(1, N):
            dp2[i][0] = nums[i]+dp2[i-1][1]
            dp2[i][1] = max(dp2[i-1])
        
        return max(dp[-1][1], dp2[-1][0])
"""
TLE
dp[i][k] := min of the largest sum among k subarrays from nums[:i]
"""
class Solution(object):
    def splitArray(self, nums, K):
        N = len(nums)
        
        dp = [[float('inf') for _ in xrange(K+1)] for _ in xrange(N+1)]
        dp[0][0] = 0
        
        for i in xrange(1, N+1):
            for k in xrange(1, min(i, K)+1):
                for j in xrange(k, i+1):
                    dp[i][k] = min(dp[i][k], max(dp[j-1][k-1], sum(nums[j-1:i])))
        
        return dp[N][K]


"""
TLE
dp[i][k] := min of the largest sum among k subarrays from nums[:i]
s[i][j] := sum of nums[i:j+1]
"""
class Solution(object):
    def splitArray(self, nums, K):
        N = len(nums)

        s = [[0 for _ in xrange(N)] for _ in xrange(N)]
        for i in xrange(N): s[i][i] = nums[i]
        for l in xrange(2, N):
            for i in xrange(N):
                j = i+l-1
                if j>=N: continue
                s[i][j] = s[i+1][j-1]+nums[i]+nums[j]

        dp = [[float('inf') for _ in xrange(K+1)] for _ in xrange(N+1)]
        dp[0][0] = 0
        
        for i in xrange(1, N+1):
            for k in xrange(1, min(i, K)+1):
                for j in xrange(k, i+1):
                    dp[i][k] = min(dp[i][k], max(dp[j-1][k-1], s[j-1][i-1]))
        
        return dp[N][K]
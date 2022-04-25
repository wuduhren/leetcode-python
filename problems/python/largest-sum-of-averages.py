"""
dp[i][k] := max score of nums[:i] using k partition.
"""
class Solution(object):
    def largestSumOfAverages(self, nums, K):
        N = len(nums)
        
        dp = [[0 for _ in xrange(K+1)] for _ in xrange(N+1)]
        for i in xrange(1, N+1): dp[i][0] = float('-inf')
        
        for i in xrange(1, N+1):
            for k in xrange(1, min(i, K)+1):
                for j in xrange(k, i+1):
                    dp[i][k] = max(dp[i][k], dp[j-1][k-1] + float(sum(nums[j-1:i]))/(i-j+1))
        
        return max(dp[N])


"""
dp[i][k] := max score of nums[:i] using k partition.
avg[i][j] := average fro nums[i:j+1]
"""
class Solution(object):
    def largestSumOfAverages(self, nums, K):
        N = len(nums)

        avg = [[0 for _ in xrange(N)] for _ in xrange(N)]
        for i in xrange(N): avg[i][i] = float(nums[i])
        
        for l in xrange(2, N+1):
            for i in xrange(N):
                j = i+l-1
                if j>=N: continue
                avg[i][j] = float((avg[i+1][j-1]*((j-1)-(i+1)+1)+nums[i]+nums[j]))/(j-i+1)
        
        dp = [[0 for _ in xrange(K+1)] for _ in xrange(N+1)]
        for i in xrange(1, N+1): dp[i][0] = float('-inf')
        
        for i in xrange(1, N+1):
            for k in xrange(1, min(i, K)+1):
                for j in xrange(k, i+1):
                    dp[i][k] = max(dp[i][k], dp[j-1][k-1] + avg[j-1][i-1])
        
        return max(dp[N])
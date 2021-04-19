"""
dp[i] = maxSumAfterPartitioning(A[0~i-1], K) and must contain A[i-1]
"""
class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        dp = [0 for _ in xrange(len(A)+1)]

        for i in xrange(1, len(A)+1):
            m = float('-inf') # max in A[i-k]~A[i-1]
            for k in xrange(1, min(i+1, K+1)):
                m = max(m, A[i-k])
                dp[i] = max(dp[i], m*k + dp[i-k])

        return dp[-1]
"""
dp[i][0] = max sum that ends at arr[i], not yet done any deletion
dp[i][1] = max sum that ends at arr[i], already done the deletion

dp[i][0] = max(dp[i-1][0]+arr[i], arr[i])
dp[i][1] = max(dp[i-1][0], dp[i-1][1]+arr[i], arr[i])

Time: O(N).
Space: O(N), can further reduce to O(1).
"""

class Solution(object):
    def maximumSum(self, arr):
        if not arr: return arr
        if len(arr)==1: return arr[0]
        
        dp = [[0, 0] for _ in xrange(len(arr))]
        subarrayMaxSum = arr[0]
        
        for i in xrange(len(arr)):
            if i==0:
                dp[i][0] = arr[i]
                dp[i][1] = arr[i]
            else:
                dp[i][0] = max(dp[i-1][0]+arr[i], arr[i])
                dp[i][1] = max(dp[i-1][0], dp[i-1][1]+arr[i])
            subarrayMaxSum = max(subarrayMaxSum, dp[i][0], dp[i][1])
        
        return subarrayMaxSum
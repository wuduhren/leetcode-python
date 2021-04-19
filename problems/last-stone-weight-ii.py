"""
dp[i][t] = considering stones[0~i-1], if it can sum up to target t

Time: O(SN), S is the sum of stone weight. N is the number of stones.
Space: O(SN), can reduce to O(S).
"""
class Solution(object):
    def lastStoneWeightII(self, stones):
        total = sum(stones)
        target = total/2
        dp = [[False for _ in xrange(target+1)] for _ in xrange(len(stones)+1)]
        dp[0][0] = True
        
        maxSum = 0
        # Keep trace of the max sum that stones can sum up to.
        
        for i in xrange(1, len(stones)+1):
            for t in xrange(target+1):
                if (dp[i-1][t] or (t-stones[i-1]>=0 and dp[i-1][t-stones[i-1]])):
                    # it can sum up to t considering stones[0~i-2]
                    # OR
                    # it can sum up to t considering stones[0~i-1]
                    dp[i][t] = True
                    maxSum = max(maxSum, t)
                    if t==target: return total-maxSum*2
        
        # Two collection of stones will be total-maxSum and maxSum
        # (total-maxSum) - maxSum => total-maxSum*2
        return total-maxSum*2

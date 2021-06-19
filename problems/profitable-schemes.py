"""
TLE
dp[i][n][p] := considering profit[:i], what is the number of ways produce profit p with n people.
"""
class Solution(object):
    def profitableSchemes(self, maxMember, minProfit, group, profit):
        P = sum(profit)
        N = sum(group)
        dp = [[[0 for _ in xrange(P+1)] for _ in xrange(N+1)] for _ in xrange(len(profit)+1)]
        dp[0][0][0] = 1
        
        count = 0
        for i in xrange(1, len(profit)+1):
            for n in xrange(N+1):
                for p in xrange(P+1):
                    dp[i][n][p] = (dp[i-1][n-group[i-1]][p-profit[i-1]] if p-profit[i-1]>=0 and n-group[i-1]>=0 else 0) + dp[i-1][n][p]
                    if i==len(profit) and p>=minProfit and n<=maxMember: count += dp[i][n][p]
        return count
        
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



"""
dp[i][g][p] := consider only crime[:i] the scheme that can generate profit p using man power g.
"""
class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        N = len(profit)
        
        dp = [[[0]*(n+2) for _ in xrange(minProfit+1)] for _ in xrange(N+1)]
        dp[0][0][0] = 1
        
        for i in xrange(1, N+1):
            for p in xrange(minProfit+1):
                for g in xrange(n+1):
                    pi = profit[i-1]
                    gi = group[i-1]
                    
                    #considerting last round using p and g
                    dp[i][p][g] += dp[i-1][p][g]
                    dp[i][min(pi+p, minProfit)][min(gi+g, n+1)] += dp[i-1][p][g]
        
        ans = 0
        for g in xrange(n+1):
            ans += dp[N][minProfit][g]
        return ans % (10**9 + 7)
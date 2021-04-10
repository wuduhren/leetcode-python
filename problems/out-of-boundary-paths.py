"""
dp[k][i][j] := number of ways to get to (i, j)
dp[k+1][i][j] = sum(dp[k][x][y]) for all (x, y) that can get to (i, j)
For each k and i and j, also accumulate the ans

Time: O(KMN)
Space: O(KMN)
"""

class Solution(object):
    def findPaths(self, M, N, K, i, j):
        ans = 0
        
        dp = [[[0 for _ in xrange(N)] for _ in xrange(M)] for _ in xrange(K+1)]
        dp[0][i][j] = 1
        
        for k in xrange(K):
            for i in xrange(M):
                for j in xrange(N):
                    if dp[k][i][j]>0:
                        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                            if x<0 or x>=M or y<0 or y>=N:
                                ans+=dp[k][i][j]
                            else:
                                dp[k+1][x][y]+=dp[k][i][j]
        return ans % (1000000007)
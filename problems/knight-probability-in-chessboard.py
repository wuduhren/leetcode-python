class Solution(object):
    def knightProbability(self, N, K, r, c):
        if K==0: return 1
        
        dp = [[[0 for _ in xrange(N)] for _ in xrange(N)] for _ in xrange(K+1)]
        
        dp[0][r][c] = 1
        possible = float(0)
        
        for k in xrange(1, K+1):
            for i in xrange(N):
                for j in xrange(N):
                    if dp[k-1][i][j]>0:
                        for x, y in [(i+1, j+2), (i-1, j+2), (i+1, j-2), (i-1, j-2), (i+2, j+1), (i-2, j+1), (i+2, j-1), (i-2, j-1)]:
                            if 0<=x and x<N and 0<=y and y<N:
                                dp[k][x][y]+=dp[k-1][i][j]
                                if k==K: possible+=dp[k-1][i][j] #calculate the possible in the last iteration.
                                
        return possible/(8**K)

"""
dp[k][i][j] := number of ways to move to (i, j) after k moves.
dp[k][i][j] = sum(dp[k-1][x][y]), for all possible (x, y) that can moves to (i, j).

Time: O(K*N^2)
Space: O(K*N^2)
"""
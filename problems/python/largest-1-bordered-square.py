class Solution(object):
    def largest1BorderedSquare(self, grid):
        if not grid or not grid[0]: return 
        M, N = len(grid), len(grid[0])
        
        dp = [[[0, 0] for _ in xrange(N+1)] for _ in xrange(M+1)]
        ans = 0
        for i in xrange(M):
            for j in xrange(N):
                if grid[i][j]==1:
                    #[0]
                    dp[i+1][j+1][0] = dp[i][j+1][0]+1
                    dp[i+1][j+1][1] = dp[i+1][j][1]+1

                    #[1]
                    K = min(dp[i+1][j+1][0], dp[i+1][j+1][1])
                    
                    #[2]
                    for k in xrange(K, -1, -1):
                        if dp[i+1-k+1][j+1][1]>=k and dp[i+1][j+1-k+1][0]>=k:
                            ans = max(ans, k**2)
                            break
                    
                elif grid[i][j]==0:
                    #[0]
                    dp[i+1][j+1][0] = 0
                    dp[i+1][j+1][1] = 0

        return ans

"""
[0]
dp[i+1][j+1][0] := number of the vertical continuous `1`s above grid[i][j]
dp[i+1][j+1][0] := number of the vertical continuous `1`s left to grid[i][j]

For each i and j
    Imagine (i, j) is the bottom-right dot of the square.
    [1] First, check the max length of the square: K. (through min(number of the vertical continuous `1`s above the bottom-right dot, number of the vertical continuous `1`s left to the bottom-right dot).)
    [2] Then, for each possible k, checking from large to small
        Get the number of the vertical continuous `1`s above the bottom-left dot.
        Get the number of the vertical continuous `1`s left to the top-right dot.
        See if they are large enough to form square with border==k.

Time: O(N^3) assume that the N is the length of the grid and grid[0].
Space: O(N^2)
"""
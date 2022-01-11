"""
dp[i][j] := considering from points[0]~points[i], the max points if choosing points[i][j]
"""
class Solution(object):
    def maxPoints(self, points):
        N = len(points)
        M = len(points[0])
        dp = [[0]*M for _ in xrange(N)]
        
        for i in xrange(N):
            for j in xrange(M):
                if i==0:
                    dp[i][j] = points[i][j]
                else:
                    dp[i][j] = points[i][j]+max([dp[i-1][k] - abs(k-j) for k in xrange(M)])
        return max(dp[N-1])

    
"""
The above solution will take O(NM^2) in time.
The bottle neck is for each j we need to traverse the whole last row.
Let us see a little bit closer on `dp[i][j]`

dp[i][j] = points[i][j]+max([dp[i-1][k] - abs(k-j) for k in xrange(M)])

So, if j>=k (Part 1)
points[i][j]+max([dp[i-1][k] - (j-k) for k in xrange(M)])
points[i][j] - j + max([dp[i-1][k] + k) for k in xrange(M)])

if k>=j (Part 2)
points[i][j] + max([dp[i-1][k] - (k-j) for k in xrange(M)])
points[i][j] + j + max([dp[i-1][k] - k) for k in xrange(M)])

Since we cannot do a full scan
why not we update the value from left to right for Part 1 and
right to left for part 2
With a variable call rollingMax to store the max.

That way dp[i][j] will be updated as if we do a full scan.

The time complexity will become O(NM)
"""
class Solution(object):
    def maxPoints(self, points):
        N = len(points)
        M = len(points[0])
        dp = [[0]*M for _ in xrange(N)]

        for j in xrange(M):
            dp[0][j] = points[0][j]
        
        for i in xrange(1, N):
            rollingMax = float('-inf')
            for j in xrange(M):
                rollingMax = max(rollingMax, dp[i-1][j] - j)
                dp[i][j] = max(dp[i][j], points[i][j] + j + rollingMax))
            
            rollingMax = float('-inf')
            for j in xrange(M, -1, -1):
                rollingMax = max(rollingMax, dp[i-1][j] + j)
                dp[i][j] = max(dp[i][j], points[i][j] - j + rollingMax))

        return max(dp[N-1])
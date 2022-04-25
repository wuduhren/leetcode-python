"""
dp[i][j] = minimum sum of falling path that chooeses A[i][j] as ending
dp[i][j] = (min(dp[i-1]) except dp[i-1][j]) + A[i][j]

implement min(dp[i-1]) except dp[i-1][j] by getMin()
Can further optimize getMin() by memorization.

Time: O(NM).
Space: O(NM), can further reduce to O(M).
"""

import collections
import heapq

class Solution(object):
    def minFallingPathSum(self, A):
        def getMin(i, j):
            minN = float('inf')
            for idx, n in enumerate(dp[i]):
                if j==idx: continue
                minN = min(minN, n)
            return minN
                
        if not A or not A[0]: return 0
        if len(A)==1: return min(A)
        
        history = collections.defaultdict(list)
        
        dp = [[0 for _ in xrange(len(A[0]))] for _ in xrange(len(A))]
        
        for i in xrange(len(A)):
            for j in xrange(len(A[0])):
                dp[i][j] = getMin(i-1, j) + A[i][j]

        return min(dp[-1])
class Solution(object):
    def minFallingPathSum(self, A):
        if not A or not A[0]: return 0
        if len(A)==1: return min(A)

        dp = [[0 for _ in xrange(len(A[0]))] for _ in xrange(len(A))]

        for i in xrange(len(A)):
            h = heapq.nsmallest(2, dp[i-1]) if i>0 else [0, 0]
            for j in xrange(len(A[0])):
                dp[i][j] = (h[1] if h[0]==dp[i-1][j] else h[0]) + A[i][j]

        return min(dp[-1])
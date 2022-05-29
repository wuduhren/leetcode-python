"""
Time: O(min(M,N)^2 * max(M,N) * Log(max(M,N)))
Space: O(MN), can reduce to O(max(M,N)) by not using a new 2D array "matrixRotated".
Just change the iteration in `maxSumSubmatrix()`.

This is the implementation of the offical solution 1 and 2.
"""
from sortedcontainers import SortedSet

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        if len(matrix)>len(matrix[0]): matrix = self.rotate(matrix)
        
        ans = float('-inf')
        M = len(matrix)
        N = len(matrix[0])
        
        for start in xrange(M):
            rowSum = [0]*N #row sum of rows from matrix[start] to row
            for row in matrix[start:]:
                for i, n in enumerate(row): rowSum[i] += n
                ans = max(ans, self.maxSumRow(rowSum, k))
                if ans==k: return ans
        return ans
    
    def maxSumRow(self, row, k):
        ans = float('-inf')
        total = 0
        
        ss = SortedSet()
        ss.add(0)
        
        for n in row:
            total += n
            i = ss.bisect_left(total-k)
            if i<len(ss):
                x = ss[i]
                ans = max(ans, total-x)
            ss.add(total)
        return ans
            
    def rotate(self, matrix):
        M = len(matrix)
        N = len(matrix[0])
        matrixRotated = [[0]*M for _ in xrange(N)]
        
        for i in xrange(M):
            for j in xrange(N):
                matrixRotated[j][i] = matrix[i][j]
        
        return matrixRotated
            
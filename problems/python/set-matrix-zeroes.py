"""
Space: O(1)
Time: O(N^2)

Mark matrix[i][0] as string if all matrix[i][?] needs to be set to 0.
Mark matrix[0][j] as string if all matrix[?][j] needs to be set to 0.
There is an edje case where matrix[0][0] cannot represent for row and col at the same time.
So we need an additional variable, firstRowToZero.

Explanation: https://www.youtube.com/watch?v=T41rL0L3Pnw
"""
class Solution(object):
    def setZeroes(self, matrix):
        firstRowToZero = False
        
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j]==0:
                    if i!=0:
                        matrix[i][0] = str(matrix[i][0])
                    else:
                        firstRowToZero = True
                    matrix[0][j] = str(matrix[0][j])
        
        
        for i in xrange(1, len(matrix)):
            if type(matrix[i][0])!=type(''): continue
            for j in xrange(len(matrix[0])): matrix[i][j] = 0
        
        for j in xrange(len(matrix[0])):
            if type(matrix[0][j])!=type(''): continue
            for i in xrange(len(matrix)): matrix[i][j] = 0
        
        if firstRowToZero:
            for j in xrange(len(matrix[0])): matrix[0][j] = 0
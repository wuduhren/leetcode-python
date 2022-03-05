class Solution(object):
    def isToeplitzMatrix(self, matrix):
        def check(i0, j0, matrix):
            i = i0
            j = j0
            
            while 0<=i<len(matrix) and 0<=j<len(matrix[0]):
                if matrix[i][j]!=matrix[i0][j0]: return False
                i += 1
                j += 1
            return True
    
        M = len(matrix)
        N = len(matrix[0])
        
        for i in xrange(M-1, 0, -1):
            if not check(i, 0, matrix): return False
        
        for j in xrange(N):
            if not check(0, j, matrix): return False
        
        return True
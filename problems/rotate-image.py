class Solution(object):
    def rotate(self, matrix):
        N = len(matrix)
        
        #transpose
        for i in xrange(N):
            for j in xrange(N):
                if j<=i: continue
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        #reflect
        for i in xrange(N):
            for j in xrange(N/2):
                matrix[i][j], matrix[i][N-1-j] = matrix[i][N-1-j], matrix[i][j]
        
        return matrix
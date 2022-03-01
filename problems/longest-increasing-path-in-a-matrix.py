class Solution(object):
    def longestIncreasingPath(self, matrix):
        def getLongest(i, j):
            if (i, j) in longest: return longest[(i, j)]
            l = 1

            #call getLongest to the neighbors that are larger than itself.
            if i+1<M and matrix[i][j]<matrix[i+1][j]:
                l = max(l, 1+getLongest(i+1, j))
            if i-1>=0 and matrix[i][j]<matrix[i-1][j]:
                l = max(l, 1+getLongest(i-1, j))
            if j+1<N and matrix[i][j]<matrix[i][j+1]:
                l = max(l, 1+getLongest(i, j+1))
            if j-1>=0 and matrix[i][j]<matrix[i][j-1]:
                l = max(l, 1+getLongest(i, j-1))
            
            longest[(i, j)] = l
            self.ans = max(self.ans, l)
            return l

        M = len(matrix)
        N = len(matrix[0])
        
        longest = {}
        self.ans = float('-inf')
        
        for i in xrange(M):
            for j in xrange(N):
                getLongest(i, j)
                
        return self.ans
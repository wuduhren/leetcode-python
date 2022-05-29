class Solution(object):
    def findDiagonalOrder(self, mat):
        def helper(i, j, reverse):
            output = []
            while 0<=i<len(mat) and 0<=j<len(mat[0]):
                output.append(mat[i][j])
                i += 1
                j -= 1
            return output if not reverse else reversed(output)
        
        
        M = len(mat)
        N = len(mat[0])
        ans = []
        reverse = True
        
        for j in xrange(N):
            ans += helper(0, j, reverse)
            reverse = not reverse
        
        for i in xrange(1, M):
            ans += helper(i, N-1, reverse)
            reverse = not reverse
        
        return ans
class Solution(object):
    def findLength(self, A, B):
        M, N = len(A), len(B)
        
        #dp[i][j] := the logest length of sub array that needs to involve A[i] and B[j]
        dp = [[0 for _ in xrange(N+1)] for _ in xrange(M+1)]
            
        for i in xrange(1, M+1):
            for j in xrange(1, N+1):
                if A[i-1]==B[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    
        return max(max(row) for row in dp)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M = len(matrix)
        N = len(matrix[0])
        firstRowZero = False
        
        for i in range(M):
            for j in range(N):
                if matrix[i][j]==0:
                    matrix[0][j] = 0                    
                    if i==0:
                        firstRowZero = True
                    else:
                        matrix[i][0] = 0
        
        for i in range(1, M):
            if matrix[i][0]==0:
                for j in range(N):
                    matrix[i][j] = 0
        
        for j in range(N):
            if matrix[0][j]==0:
                for i in range(M):
                    matrix[i][j] = 0
        
        if firstRowZero:
            for j in range(N):
                matrix[0][j] = 0
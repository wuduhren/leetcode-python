class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N = len(matrix)
        M = len(matrix[0])
        
        l = 0
        r = N*M-1
        
        while l<=r:
            m = l + int((r-l)/2)
            
            i = int(m/M)
            j = m%M
            
            if matrix[i][j]<target:
                l = m+1
            elif matrix[i][j]>target:
                r = m-1
            else:
                return True
        
        return False
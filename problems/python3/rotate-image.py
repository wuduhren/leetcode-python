class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix[0])-1
        
        while l<r:
            top = l
            bottom = r
            for i in range(r-l):
                topLeft = matrix[top][l+i]
                matrix[top][l+i] = matrix[bottom-i][l]
                matrix[bottom-i][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = topLeft
            l += 1
            r -= 1
            #the outer layer is finisthed, going into the inner layer
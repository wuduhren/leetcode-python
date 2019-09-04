"""
First I decided to flatten the matrix to an 1-D array, `A`.
Because it is easier to navigate in this structure.
And because `A` is already sorted, we can aplly binary search here.
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        A = []
        for row in matrix: A.extend(row)

        l = 0
        r = len(A)-1
        while l<=r:
            m = (l+r)/2
            if A[l]==target: return True
            if A[m]==target: return True
            if A[r]==target: return True

            if A[m]>target:
                r = m-1
            else:
                l = m+1
        return False

class Solution(object):
    def searchMatrix(self, matrix, target):
        def getMatrix(i):
            n = i/M
            m = i%M
            return matrix[n][m]

        if not matrix or len(matrix)==0 or len(matrix[0])==0: return False

        N = len(matrix)
        M = len(matrix[0])

        l = 0
        r = N*M-1
        while l<=r:
            p = (l+r)/2
            if getMatrix(l)==target: return True
            if getMatrix(p)==target: return True
            if getMatrix(r)==target: return True

            if getMatrix(p)>target:
                r = p-1
            else:
                l = p+1
        return False

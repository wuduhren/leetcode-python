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


#2020/7/23
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        
        #if you do not understand binary search yet, please study it first.
        #use binary search to find the list that has target.
        #if found, asign it to A.
        l = 0
        r = len(matrix)-1
        A = None
        while l<=r:
            if matrix[l][0]<=target and target<=matrix[l][-1]:
                A = matrix[l]
                break
            if matrix[r][0]<=target and target<=matrix[r][-1]:
                A = matrix[r]
                break
            
            m = (l+r)/2
            
            if matrix[m][0]<=target and target<=matrix[m][-1]:
                A = matrix[m]
                break
            elif target<matrix[m][0]:
                r = m-1
            else:
                l = m+1
        
        if not A: return False
        
        #find if target in A
        l = 0
        r = len(A)-1
        while l<=r:
            if target==A[l] or target==A[r]: return True
            
            m = (l+r)/2
            
            if target==A[m]:
                return True
            elif target<A[m]:
                r = m-1
            else:
                l = m+1
        return False
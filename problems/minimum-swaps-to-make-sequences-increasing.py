class Solution(object):
    def minSwap(self, A, B):
        keep = [float('inf') for _ in xrange(len(A))]
        swap = [float('inf') for _ in xrange(len(A))]
        
        keep[0] = 0
        swap[0] = 1
        
        for i in xrange(1, len(A)):
            
            if A[i]>A[i-1] and B[i]>B[i-1]:
                keep[i] = keep[i-1]
                swap[i] = swap[i-1]+1
                
            if A[i]>B[i-1] and B[i]>A[i-1]:
                keep[i] = min(keep[i], swap[i-1])
                swap[i] = min(swap[i], keep[i-1]+1)
                
        return min(keep[-1], swap[-1])
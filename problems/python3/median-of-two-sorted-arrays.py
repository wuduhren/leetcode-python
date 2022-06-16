class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        if len(A)>len(B): A, B = B, A
        
        total = len(A)+len(B)
        half = total//2
        l = 0
        r = len(A)-1
        
        while True:
            i = l + (r-l)//2
            j = half-(i+1)-1
            
            Aleft = A[i] if i>=0 else float('-inf')
            Aright = A[i+1] if i+1<len(A) else float('inf')
            Bleft = B[j] if j>=0 else float('-inf')
            Bright = B[j+1] if j+1<len(B) else float('inf')
            
            if Aleft<=Bright and Bleft<=Aright:
                if total%2==0:
                    return (max(Aleft, Bleft)+min(Aright, Bright))/2
                else:
                    return min(Aright, Bright)
            elif Aleft>Bright:
                r = i-1
            else:
                l = i+1
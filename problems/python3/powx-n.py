class Solution:
    def myPow(self, x: float, k: int) -> float:
        if k<0: return 1/self.myPow(x, -k)

        if k==0:
            return 1
        elif k==1:
            return x
        elif k%2==0:
            half = self.myPow(x, k//2)
            return half * half
        else:
            half = self.myPow(x, (k-1)//2) 
            return half * half * x
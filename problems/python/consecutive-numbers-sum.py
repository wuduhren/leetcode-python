
# Sliding window
class Solution(object):
    def consecutiveNumbersSum(self, N):
        i = 1
        j = 2
        s = 1 #sum(range(i, j))
        ans = 0
        
        while i<=j and j<=N+1:
            if s==N:
                ans += 1
                s += j
                j += 1
            elif s>N:
                s -= i
                i += 1
            else:
                s += j
                j += 1
        return ans


#Math
class Solution(object):
    def consecutiveNumbersSum(self, N):
        ans = 0
        upperLimit = int((2 * N + 0.25)**0.5 - 0.5) + 2
        
        for x in xrange(1, upperLimit):
            if x%2==0:
                if float(N)/x-N/x==0.5:
                    upper = N/x + x/2
                    lower = N/x - x/2 + 1
                    if 1<=lower and upper<=N:
                        ans += 1
            else:
                if N%x==0:
                    upper = N/x + (x-1)/2
                    lower = N/x - (x-1)/2
                    if 1<=lower and upper<=N: 
                        ans += 1
        return ans
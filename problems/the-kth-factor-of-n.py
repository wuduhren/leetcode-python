"""
Time: O(N)
Space: O(F), storing number of factors for N.
"""
class Solution(object):
    def kthFactor(self, n, k):
        factors = []
        
        for i in xrange(1, n+1):
            if n%i==0:
                factors.append(i)
                if len(factors)==k: return factors[-1]
        return -1


"""
Time: O(N^1/2)
Space: O(F), storing number of factors for N.
"""
class Solution(object):
    def kthFactor(self, n, k):
        factors1 = []
        factors2 = []
        
        for i in xrange(1, int(n**0.5)+1):
            if n%i==0:
                factors1.append(i)
                if i!=n/i: factors2.append(n/i)
        
        factors = factors1+factors2[::-1] 
        
        return factors[k-1] if k-1<len(factors) else -1
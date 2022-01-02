class Solution(object):
    def uniquePaths(self, m, n):
        def factorial(n):
            ans = 1
            for i in xrange(1, n+1):
                ans *= i
            return ans
        
        return factorial((m-1)+(n-1))/(factorial(n-1)*factorial(m-1))
class Solution(object):
    def countOrders(self, n):
        d = 1
        for i in xrange(1, 2*n, 2): d*=i
        return math.factorial(n)*d % (10**9 + 7)
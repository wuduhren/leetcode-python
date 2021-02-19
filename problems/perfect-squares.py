#Recursive
class Solution(object):
    def numSquares(self, n):
        def helper(n):
            if not n: return 0
            if n in history: return history[n]
            
            elements = [e**2 for e in range(2, int(n**0.5)+1)]
            ans = n

            for e in reversed(elements):
                count_of_element = int(n/e)
                n_approximate = count_of_element*e
                ans = min(ans, count_of_element+helper(n-n_approximate))
            
            history[n] = ans
            return history[n]
        
        history = {1:1, 2:2, 3:3}
        return helper(n)

#DP
class Solution(object):
    def numSquares(self, N):
        squares = [s**2 for s in range(2, int(N**0.5)+1)]
        
        dp = [n for n in xrange(N+1)]
        
        for n in xrange(N+1):
            for square in squares:
                if square>n:
                    break
                elif square==n:
                    dp[n] = 1
                    break
                else:
                    dp[n] = min(dp[n], dp[square]+dp[n-square])
        return dp[N]
        
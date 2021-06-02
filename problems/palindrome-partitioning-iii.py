"""
dp[i][k] :=  the minimal number of characters that needed to change for s[:i] with k disjoint substrings
"""
class Solution(object):
    def palindromePartition(self, s, K):
        def count(r, l):
            c = 0
            
            while r>l:
                if s[r]!=s[l]: c += 1
                r -= 1
                l += 1
            return c

        N = len(s) 
        
        dp = [[float('inf') for _ in xrange(K+1)] for _ in xrange(N+1)]
        dp[0][0] = 0
        
        for i in xrange(1, N+1):
            for k in xrange(1, min(K, i)+1):
                for j in xrange(k, i+1):
                    dp[i][k] = min(dp[i][k], dp[j-1][k-1] + count(i-1, j-1))
                    
        return dp[N][K]

"""
The above `count()` are able to use dp technique to optimize.
dp[i][k] :=  the minimal number of characters that needed to change for s[:i] with k disjoint substrings
count[i][j] := the operation needed for s[i:j+1] become palindrome.
"""
class Solution(object):
    def palindromePartition(self, s, K):
        N = len(s)

        count = [[0 for _ in xrange(N)] for _ in xrange(N)]
        for i in xrange(N): count[i][i] = 0

        for l in xrange(2, N+1):
            for i in xrange(N):
                j = i+l-1
                if j>=N: continue
                count[j][i] = count[j-1][i+1] + (0 if s[i]==s[j] else 1)
        
        dp = [[float('inf') for _ in xrange(K+1)] for _ in xrange(N+1)]
        dp[0][0] = 0
        
        for i in xrange(1, N+1):
            for k in xrange(1, min(K, i)+1):
                for j in xrange(k, i+1):
                    dp[i][k] = min(dp[i][k], dp[j-1][k-1] + count[i-1][j-1])
                    
        return dp[N][K]
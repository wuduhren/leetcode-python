
# Implement from https://www.youtube.com/watch?v=GgP75HAvrlY
class Solution(object):
    def numTrees(self, n):
        dp = [1, 1, 2]
        
        if n<=2: return dp[n]
        
        for i in xrange(3, n+1):
            dp.append(0)
            for root in xrange(1, i+1):
                dp[i] += dp[root-1]*dp[i-root]
                
        return dp[n]

"""
dp[n] := the number of structurally unique BST's which has n nodes with val 1~n
dp[n] = helper(n)

Form 1~n nodes
If we use 1 as root, the left subtree possible count will be dp[1-1] and right subtree be dp[n-1], the count will be dp[0]*dp[n-1].
If we use 2 as root, the left subtree possible count will be dp[2-1] and right subtree be dp[n-2], the count will be dp[1]*dp[n-2].
If we use 3 as root, the left subtree possible count will be dp[3-1] and right subtree be dp[n-3], the count will be dp[2]*dp[n-3].
...
If we use i as root, the left subtree possible count will be dp[i-1] and right subtree be dp[n-i], the count will be dp[i-1]*dp[n-i].

So the number of structurally unique BST's which has n nodes with val 1~n, will be the sum above.

Time: O(N^2)
Space: O(N)
"""
class Solution(object):
    def numTrees(self, N):
        def helper(n):
            count = 0
            for i in xrange(1, n+1):
                count += dp[i-1]*dp[n-i]
            return count
                
        dp = [0]*(N+1)
        dp[0] = 1
        dp[1] = 1
        
        for n in xrange(2, N+1):
            dp[n] = helper(n)
        return dp[N]
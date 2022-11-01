"""
dp[i] := up until s[:i] how many possibility?
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        mapping = set([str(n) for n in range(1, 27)])
        N = len(s)
        dp = [0]*(N+1)
        dp[0] = 1
        
        for i in range(1, N+1):
            if i-1>=0 and s[i-1] in mapping: dp[i] += dp[i-1]
            if i-2>=0 and s[i-2:i] in mapping: dp[i] += dp[i-2]
        return dp[-1]
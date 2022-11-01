class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #dp[i][j] := number of longest Common Subsequence with text2[:i] and text2[:j]
        
        N = len(text1)
        M = len(text2)
        
        dp = [[0]*(M+1) for _ in range(N+1)]
        
        for i in range(1, N+1):
            for j in range(1, M+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]
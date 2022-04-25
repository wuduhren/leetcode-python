class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        M, N = len(text1), len(text2)
        
        #dp[i][j] := logest subsequence of text1[0:i-1] and text[0:j-1]
        dp = [[0 for _ in xrange(N+1)] for _ in xrange(M+1)]
            
        for i in xrange(1, M+1):
            for j in xrange(1, N+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[M][N]

"""
Time: O(MN)
Space: O(MN)
"""

 
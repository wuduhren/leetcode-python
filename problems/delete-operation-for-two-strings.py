class Solution(object):
    def minDistance(self, word1, word2):
        N = len(word1)
        M = len(word2)
        
        dp = [[float('inf') for _ in xrange(M+1)] for _ in xrange(N+1)]
        
        
        for i in xrange(1, N+1): dp[i][0] = i #need i deletion for word1[0:i-1] to be ""
        for j in xrange(1, M+1): dp[0][j] = j #need i deletion for word1[0:j-1] to be ""
        dp[0][0] = 0
        
        for i in xrange(1, N+1):
            for j in xrange(1, M+1):
			    #dp[i][j] := min operation count for dp[0:i] and dp[0:j-1] to be the same.
                
				#if char at i-1 and j-1 are the same, no deletion needed.
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                
                dp[i][j] = min(dp[i][j], dp[i][j-1]+1) #remove char on word2[j-1]
                dp[i][j] = min(dp[i][j], dp[i-1][j]+1) #remove char on word1[i-1]
            return dp[N][M]

"""
Time: O(MN)
Space: O(MN)
"""
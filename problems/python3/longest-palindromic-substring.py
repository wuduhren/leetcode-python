"""
Time: O(N^2)
Space: O(N^2)

DP, TLE
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        N = len(s)
        dp = [[False]*N for _ in range(N)]
        
        for i in range(N): dp[i][i] = True
        
        for l in range(2, N+1):
            for i in range(N):
                j = i+l-1
                if j>=N: continue
                dp[i][j] = s[i]==s[j] and (dp[i+1][j-1] or j-1<i+1)
                if dp[i][j]: ans = s[i:j+1]
        return ans


"""
Time: O(N^2)
Space: O(1)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        ans = s[0]
        
        for i in range(N):
            l, r = i, i
            while l>=0 and r<N and s[l]==s[r]:
                if r-l+1>len(ans): ans = s[l:r+1]
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l>=0 and r<N and s[l]==s[r]:
                if r-l+1>len(ans): ans = s[l:r+1]
                l -= 1
                r += 1
        return ans
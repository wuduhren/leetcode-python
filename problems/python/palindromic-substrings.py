"""
dp[i][j] := if s[i:j+1] is palindrome.
1. all length==1 string is palindrome.
2. all length==2 string is palindrome if two are the same.
3. all length>=3 string is palindrome if the outer most two char is the same and have an palindrome string inside.

Time: O(N^2)
Space: 0(N^2)
"""
class Solution(object):
    def countSubstrings(self, s):
        N = len(s)
        dp = [[False]*N for _ in xrange(N)]
        ans = 0
        
        #1
        for i in xrange(N):
            dp[i][i] = True
            ans += 1
        
        #2
        for i in xrange(N-1):
            if s[i]==s[i+1]:
                dp[i][i+1] = True
                ans += 1
        
        #3
        for l in xrange(3, N+1):
            for i in xrange(N):
                j = i+l-1
                if j>=N: continue
                if dp[i+1][j-1] and s[i]==s[j]:
                    dp[i][j] = True
                    ans += 1
        return ans

"""
Iterate through the string, expand around each character.
Like this solution more since it is more intuitive.

Time: O(N^2)
Space: O(1)
"""
class Solution(object):
    def countSubstrings(self, s):
        def count(l, r, N):
            count = 0
            
            while l>=0 and r<N and s[l]==s[r]:
                count += 1
                l = l-1
                r = r+1
            return count
                
        N = len(s)
        ans = 0
        
        for i in xrange(N):
            ans += count(i, i+1, N) #count even length palindrome
            ans += count(i, i, N) #count odd length palindrome
        return ans
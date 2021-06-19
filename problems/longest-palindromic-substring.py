"""
findPalindorome() find the palindrone string from the center "mid"
The center could be one char (case 1) or two the same char (case 2)
We iterate through every char in string and assume it is the center
And put it in findPalindorome() to find the longest

Time Efficiency: O(N^2)
Space Efficiency: O(N)
"""
class Solution(object):
    def longestPalindrome(self, s):
        def findPalindorome(mid, mid2=None):
            r = 0
            l = len(s)
            max_pal = ''

            if mid2:
                #case 2
                if mid<0 or mid>=l: return ''
                if mid2<0 or mid2>=l: return ''
                while mid-r>=0 and mid2+r<l and s[mid-r]==s[mid2+r]:
                    max_pal = s[mid-r:mid2+r+1]
                    r+=1
            else:
                #case 1
                if mid<0 or mid>=l: return ''
                while mid-r>=0 and mid+r<l and s[mid-r]==s[mid+r]:
                    max_pal = s[mid-r:mid+r+1]
                    r+=1
            return max_pal
                
        max_pal = ''
        l = len(s)
        for i in range(len(s)):
            #case 1
            p = findPalindorome(i)
            max_pal = p if len(p)>len(max_pal) else max_pal

            #case 2
            p2 = findPalindorome(i, i+1)
            max_pal = p2 if len(p2)>len(max_pal) else max_pal
            
        return max_pal


#2021/6/18 DP TLE
"""
dp[i][j] := if s[i:j+1] is palindrom
"""
class Solution(object):
    def longestPalindrome(self, s):
        if not s: return s
        
        N = len(s)
        dp = [[False for _ in xrange(N+1)] for _ in xrange(N+1)]
        for i in xrange(N+1): dp[i][i] = True
        ans = s[0]    
        
        for l in xrange(2, N+1):
            for i in xrange(1, N+1):
                j = i+l-1
                if j>N: continue
                dp[i][j] = s[i-1]==s[j-1] and (dp[i+1][j-1] or j-1<i+1)
                if dp[i][j]: ans = s[i-1:j]
        
        return ans
class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindrome(l, r) -> int:
            count = 0
            while l>=0 and r<N and s[l]==s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        
        N = len(s)
        ans = 0
        for i in range(N):
            ans += countPalindrome(i, i)
            ans += countPalindrome(i, i+1)
        return ans
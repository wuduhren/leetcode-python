"""
When seeing the first different chars in the string.
Check if anyone of the string is palindrome if we remove one of them.

Time: O(N)
Space: O(1)
"""
class Solution(object):
    def validPalindrome(self, s):
        def isPalindrome(s):
            i = 0
            j = len(s)-1
            while i<j:
                if s[i]!=s[j]: return False
                i += 1
                j -= 1
            return True
        
        i = 0
        j = len(s)-1
        
        while i<j:
            if s[i]==s[j]:
                i += 1
                j -= 1
            else:
                return isPalindrome(s[i:j]) or isPalindrome(s[i+1:j+1])
            
        return True
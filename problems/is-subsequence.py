class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        
        for c in t:
            if i>=len(s): break
            if s[i]==c: i += 1
        
        return i==len(s)
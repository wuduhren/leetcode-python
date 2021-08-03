"""
The description of the problem is unclear, let me rephrase it.

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t and t can be replaced to get s.

For each replacement, the characters in the same string must be replaced with another character while preserving the order of characters.
No two characters in the same string may map to the same character, but a character may map to itself.

Two replacement are independent from each other. In other words, s -> t and t -> s does not affect each other.
"""

"""
Time: O(N)
Space: O(N)
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)!=len(t): return False
        
        # check if s1 chars could be replaced and become s2
        def helper(s1, s2):
            memo = {}
            
            for i in xrange(len(s)):
                c1 = s1[i]
                c2 = s2[i]
                
                if c1 in memo and memo[c1]!=c2: return False
                memo[c1] = c2
            return True
        
        return helper(s, t) and helper(t, s)
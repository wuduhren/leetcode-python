"""
`p` is the index on s which already processed.
"""
class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        p = -1
        ans = ''
        
        memo = {}
        for i, index in enumerate(indices):
            memo[index] = (sources[i], targets[i])
        
        for i in xrange(len(s)):
            if i<=p: continue
            
            if i in memo and (s[i:i+len(memo[i][0])] if i+len(memo[i][0])<len(s) else s[i:])==memo[i][0]:
                ans += memo[i][1]
                p = i+len(memo[i][0])-1
            else:
                ans += s[i]
                p = i
            
        return ans

"""
Time: O(N). N is the length of `s`. The replacement won't be more than the length of the string, Let's assume it is N.
Space: O(N).
"""
class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        ans = ''
        
        replacement = {}
        for i in xrange(len(indices)):
            index = indices[i]
            source = sources[i]
            target = targets[i]
            
            if s[index:index+len(source)]!=source: continue
            replacement[index] = (source, target)
        
        i = 0
        while i<len(s):
            if i not in replacement:
                ans += s[i]
                i += 1
            else:
                ans += replacement[i][1]
                i += len(replacement[i][0])
        
        return ans
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
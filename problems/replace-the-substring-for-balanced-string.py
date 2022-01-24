class Solution(object):
    def balancedString(self, s):
        n = len(s)
        counter = collections.Counter(s)
        i = 0
        ans = n
        
        for j, c in enumerate(s):
            counter[c] -= 1
            
            while i<n and all(counter[c]<=n/4 for c in 'QEWR'):
                counter[s[i]] += 1
                ans = min(ans, j-i+1)
                i += 1
        return ans
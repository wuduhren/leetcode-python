class Solution(object):
    def countBinarySubstrings(self, s):
        groups = []
        count = 0
        last = s[0]
        ans = 0
        
        for bit in s:
            if bit==last:
                count += 1
            else:
                groups.append(count)
                count = 1
            last = bit
        
        groups.append(count)
        
        for i in xrange(1, len(groups)):
            ans += min(groups[i], groups[i-1])
        
        return ans
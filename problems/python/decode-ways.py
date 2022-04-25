"""
Time: O(N), due to the "memo", the time can reduce from O(2^N) to O(N).
Space: O(N)
"""
class Solution(object):
    def numDecodings(self, s):
        def helper(s, i):
            if (s, i) in memo: return memo[(s, i)]
            if i>=len(s): return 1
            if s[i]=='0': return 0
            
            count = 0
            count += helper(s, i+1)
            if len(s)-i>=2 and int(s[i:i+2])<=26: count += helper(s, i+2)
            memo[(s, i)] = count
            return count
                
        memo = {}
        return helper(s, 0)
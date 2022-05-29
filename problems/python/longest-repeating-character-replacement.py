"""
Use the sliding window to iterate over the sub-strings. At the same time use a counter to track the count.
The operation needed is the (length of the window) -  (count of the max count char in the counter)
Since there are at most 26 char in the counter, `max(counter.values())` can be view as a O(1) operation.

Time: O(N)
Space: O(N)
"""
class Solution(object):
    def characterReplacement(self, s, k):
        counter = collections.Counter()
        ans = 0
        
        l = 0
        for r in xrange(len(s)):
            counter[s[r]] += 1
            
            while r-l+1-max(counter.values())>k:
                counter[s[l]] -= 1
                l += 1
                
            ans = max(ans, r-l+1)
        return ans
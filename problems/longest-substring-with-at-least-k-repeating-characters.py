"""
Time: O(N^2) (Worst case). O(N) (Best case)
Space: O(N)

The "Substring" must be a continuous part of s.
If a certain char with index i does not have count>=k, the answer must be in `s[:i]` or `s[i+1:]`.
"""
import collections

class Solution(object):
    def longestSubstring(self, s, k):
        if not s: return 0
        counter = collections.Counter(s)
        
        i = 0
        while i<len(s):
            c = s[i]
            
            if counter[c]>=k:
                i += 1
            else:
                return max(self.longestSubstring(s[:i], k), self.longestSubstring(s[i+1:], k))
        return i

"""
Optimize the above solution to using O(1) space by pointers `l` and `r`
"""
class Solution(object):
    def longestSubstring(self, s, k):
        def helper(l, r):
            if r-l==0: return 0
            counter = collections.Counter(s[l:r])
            
            i = l
            while i<r:
                c = s[i]
                
                if counter[c]>=k:
                    i += 1
                else:
                    return max(helper(l, i), helper(i+1, r))
            return i-l
        
        return helper(0, len(s))

"""
Time: O(N). Each `helper()` takes O(N), uniqueCount will be at most 26, O(26N) ~= O(N).
Space: O(N).

Use a sliding window (`s[i:j+1]`) to go through `s`.
Givin a fixed i we move the j as right as possible. Then move the i right (Before we move the i, recalculate a those var tracking s[i:j+1]) [0]
For each sliding window if all the unique char has count>=k (`len(counter)==m and count==m`), update the answer.

What is "m"?
Without "m", you will soon notice that we are not able to stop sliding window growing.
So we need to add the constraint: Get longestSubstring with m unique char. [1]
The final answer will be the max of:
longestSubstring with 1 unique char.
longestSubstring with 2 unique char.
...
...
longestSubstring with uniqueCount unique char.
"""
class Solution(object):
    def longestSubstring(self, s, k):
        ans = 0
        uniqueCount = len(set(s))
        
        for m in xrange(1, uniqueCount+1):
            ans = max(ans, self.helper(s, k, m))
            
        return ans
    
    #[1]
    def helper(self, s, k, m):
        j = 0
        counter = collections.Counter() #count each char in s[i:j+1]
        countOverK = 0 #number of char in s[i:j+1] count>=k
        ans = 0
        
        for i in xrange(len(s)):
            while j<len(s) and len(counter)<=m:
                counter[s[j]] += 1
                
                if counter[s[j]]==k: countOverK += 1
                
                #all char in the sliding window has count larger or equal to k.
                if len(counter)==m and countOverK==m: ans = max(ans, j-i+1)
                
                j += 1
            
            #[0]
            counter[s[i]] -= 1
            if counter[s[i]]==k-1: countOverK -= 1
            if counter[s[i]]==0: counter.pop(s[i], None)
                
        return ans
"""
Time: O(N)
Space: O(N)

`counter1` counts the char in `s1`
`counter2` counts the char is `s2[i:j+1]`

Create a sliding window with length `len(s1)`, l. From i to j.
Move the sliding window (`s2[i:j+1]`) from left to right while maintaining counter2.
Each iteration, add s2[j] to the sliding window.
At the end of iteration, remove s2[i] from the sliding window.
If two counter are the same, s1 and s2[i:j+1] are permutations of each other.
"""
import collections

class Solution(object):
    def checkInclusion(self, s1, s2):
        l = len(s1)
        counter1 = collections.Counter(s1)
        counter2 = collections.Counter(s2[:l-1])
        
        for i in xrange(len(s2)):
            j = i+l-1
            if j>=len(s2): break
            counter2[s2[j]] += 1
            
            if counter1==counter2: return True
            
            counter2[s2[i]] -= 1
            if counter2[s2[i]]==0: counter2.pop(s2[i], None)
            
        return False
"""
Time: O(N+K), N is the length. K is the updates count.
Space: O(N)

The bottleneck of the naive solution is that each "update" takes O(N) time to traverse from s to e.
The to total time complexity will become O(NK).
So we need to find a way to summarize the updates and apply those at once...

Declare updateSummary, I will store the all the updates in it.

Given length equals to 10: [0,0,0,0,0,0,0,0,0,0]
For update (1,3,4), you can also see it as
[0,+4,+4,+4,+4,+4,+4,+4,+4,+4] (Add 4 to all element after and including) index 1)
[0,0,0,0,-4,-4,-4,-4,-4,-4] (Remove 4 to all element after index 3)
And we can summarize this in updateSummary as [0,4,0,0,-4,0,0,0,0,0]

For update (0,2,-2), you can also see it as
[-2,-2,-2,-2,-2,-2,-2,-2,-2,-2] (Add -2 to all element after and including index 0)
[0,0,0,+2,+2,+2,+2,+2,+2,+2] (Remove -2 to all element after index 2)
And we can summarize this in updateSummary as [-2,0,0,+2,0,0,0,0,0,0]

updateSummary[i] means adding value updateSummary[i] to all index after and including i in ans.
"""
class Solution(object):
    def getModifiedArray(self, length, updates):
        ans = [0]*length
        updateSummary = [0]*length
        
        for s, e, v in updates:
            updateSummary[s] += v
            if e+1<len(updateSummary): updateSummary[e+1] -= v
        
        temp = 0
        for i in xrange(len(ans)):
            temp+=updateSummary[i]
            ans[i] = temp
        
        return ans

"""
Time: O(N+K)
Space: O(1)

Further more, we can store updateSummary in ans before we asign value to ans to save space.
"""
class Solution(object):
    def getModifiedArray(self, length, updates):
        ans = [0]*length
        
        for s, e, v in updates:
            ans[s] += v
            if e+1<len(ans): ans[e+1] -= v
        
        temp = 0
        for i in xrange(len(ans)):
            temp+=ans[i]
            ans[i] = temp
        
        return ans
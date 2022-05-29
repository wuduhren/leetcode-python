"""
First, reverse sort the list and iterate though it.
i = 0, if 1>=citations[i], it means that at least 1 of the citations is larger than 1.
i = 1, if 2>=citations[i], it means that at least 2 of the citations is larger than 2.
i = 3, if 3>=citations[i], it means that at least 3 of the citations is larger than 3.
...
...
Keep iterating until we fail the condition.

Time: O(NLogN)
Space: O(1)
"""
class Solution(object):
    def hIndex(self, citations):
        citations.sort(reverse=True)
        
        ans = 0
        for i in xrange(len(citations)):
            if i+1>citations[i]: break
            ans = i+1
                
        return ans


"""
First, count each citation and store it in counter.
The citation that is larger than N will be stored to N. [0]
Since for citations, the max possible h-index will be N (the length of the citations).
This can greatly reduce the index we go through when we iterate through counter.

Second, since the max possible h-index is N, we start from N and iterate to 0.
Check if any of them is answer

Time: O(N)
Space: O(N)
"""
import collections

class Solution(object):
    def hIndex(self, citations):
        counter = collections.Counter() #count for each citation
        N = len(citations)
        count = 0
        
        for citation in citations:
            counter[min(N, citation)] += 1 #[0]
            
        for n in xrange(N, -1, -1):
            count += counter[n] #count of citation that is larger or equal to n
            if count>=n: return n
        
        return 0
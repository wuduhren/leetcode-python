"""
Time: O(N)
Space: O(N)

For each char, store its max index in maxIndex.
Iterate through the string, update the "currMax" along the way.
currMax is the place we can partition unless it get updated again.
If the current index is the currMax, update "ans".
"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        maxIndex = {}
        
        for i, c in enumerate(s):
            maxIndex[c] = i
        
        currMax = 0
        processedLength = 0
        for i, c in enumerate(s):
            currMax = max(currMax, maxIndex[c])
            if i==currMax:
                ans.append(i+1 - processedLength)
                processedLength += ans[-1]

        return ans
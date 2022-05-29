"""
1. Find each char's ranges. Store into `charRange`.
2. Merge the ranges. Store into `r`.
3. Change the `r` format.

For example:
The input is "ababcbacadefegdehijhklij"
charRange will be: `{'a': [0, 8], 'c': [4, 7], 'b': [1, 5], 'e': [10, 15], 'd': [9, 14], 'g': [13, 13], 'f': [11, 11], 'i': [17, 22], 'h': [16, 19], 'k': [20, 20], 'j': [18, 23], 'l': [21, 21]}`
After merging above the range should be `[[0, 8], [9, 15], [16, 23]]`. And store it in `r`: `[8, 15, 23]`.
`ans` will be `[9,7,8]`
"""
class Solution(object):
    def partitionLabels(self, s):
        charRange = {}
        r = []
        
        for i, c in enumerate(s):
            if c not in charRange:
                charRange[c] = [i, i]
            else:
                charRange[c][1] = i
        
        for i, c in enumerate(s):
            if i==0 or charRange[c][0]>r[-1]:
                r.append(charRange[c][1])
            else:
                r[-1] = max(r[-1], charRange[c][1])
        
        ans = []
        for i in xrange(len(r)):
            if i==0:
                ans.append(r[i]+1)
            else:
                ans.append(r[i]-r[i-1])
        return ans

"""
This offical answer is even cleaner.
"""
class Solution(object):
    def partitionLabels(self, s):
        lastSeen = {}
        for i, c in enumerate(s): lastSeen[c] = i
        
        ans = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, lastSeen[c])
            if i==end:
                ans.append(end-start+1)
                start = i+1
        return ans
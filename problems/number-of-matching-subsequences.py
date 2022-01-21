"""
Time: O(WL x LogS), W is the length of words, L is the length of word.
LogS is the time for binary search and S should be the count of repetitive words, we can assume it is Log(S/26) ~= LogS.

Space: O(S)
"""
class Solution(object):
    def numMatchingSubseq(self, s, words):
        def match(position, word):
            prev = -1
            for c in word:
                if c not in position: return False
                i = bisect.bisect_left(position[c], prev+1)
                if i==len(position[c]): return False
                prev = position[c][i]
            return True
        
        position = collections.defaultdict(list)
        count = 0
        for i, c in enumerate(s):
            position[c].append(i)
        
        for word in words:
            if match(position, word): count += 1
        return count
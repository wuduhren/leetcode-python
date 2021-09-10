"""
Time: O(1)
Space: O(1), no "extra" space are used.
"""
class Solution(object):
    def readBinaryWatch(self, turnedOn):
        ans = []
        if turnedOn>8: return ans #at most 8 LED are turned on for a valid time.

        for h in xrange(12):
            for m in xrange(60):
                if (bin(h) + bin(m)).count('1')==turnedOn:
                    ans.append('%d:%02d' % (h, m))
        return ans
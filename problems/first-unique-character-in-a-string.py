import collections

class Solution(object):
    def firstUniqChar(self, string):
        counter = collections.Counter()
        for char in string:
            counter[char]+=1

        for i in xrange(len(string)):
            char = string[i]
            if counter[char]==1: return i

        return -1

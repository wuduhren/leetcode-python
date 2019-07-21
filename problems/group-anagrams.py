#https://leetcode.com/problems/group-anagrams/
class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = collections.defaultdict(list)
        for s in strs:
            anagrams[''.join(sorted(s))].append(s)
        return anagrams.values()

class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = collections.defaultdict(list)
        for s in strs:
            hashkey = [0]*26
            for c in s: hashkey[ord(c)-97] +=1
            anagrams[''.join(hashkey)].append(s)
        return anagrams.values()

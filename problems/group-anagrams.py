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

"""
Time: O(NK), N is the number of strings, K is the number of characters in the string.
Space: O(NK).
"""
class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = collections.defaultdict(list)
        
        for s in strs:
            anagrams[self.getKey(s)].append(s)
        
        return anagrams.values()
    
    def getKey(self, s):
        key = ''
        counts = collections.Counter(s)
        for c in 'abcdefghijklmnopqrstuvwxyz':
            key += counts[c]*c
        return key
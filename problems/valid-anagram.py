#https://leetcode.com/problems/valid-anagram/
class Solution(object):
    
    #1
    #O(NlogN)
    def isAnagram(self, s, t):
        if len(s)!=len(t): return False
        return sorted(s)==sorted(t)
        
    #2
    #O(N)
    #using counter
    def isAnagram(self, s, t):
        if len(s)!=len(t): return False
        
        counter1 = collections.Counter()
        counter2 = collections.Counter()
        for c in s:
            counter1[c]+=1
        for c in t:
            counter2[c]+=1
            
        return counter1==counter2
    
    #3
    #this is the same as the above solution
    #but even more clean
    #O(N)
    def isAnagram(self, s, t):
        return collections.Counter(s)==collections.Counter(t)

    
    #4
    #this is the best solution so far
    #python handle string fast bc its written in c a bottom
    #O(26N)≈O(N)
    def isAnagram(self, s, t):
        if len(s)!=len(t): return False
        for i in string.ascii_lowercase:
                if s.count(i) != t.count(i):
                    return False
        return True


#2021//7/29
"""
Time: O(N)
Space: O(N)
"""
import collections

class Solution(object):
    def isAnagram(self, s, t):
        counter = collections.Counter()
        if len(t)>len(s): t, s = s, t
        
        for c in s: counter[c] += 1
        for c in t: counter[c] -= 1
        for c in counter:
            if counter[c]>0: return False
        return True
        
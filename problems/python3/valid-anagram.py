class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = collections.Counter()
        
        for c in s:
            counter[c] += 1
        
        for c in t:
            if c not in counter:
                return False
            counter[c] -= 1
        
        for c in counter:
            if counter[c]>0:
                return False
        
        return True
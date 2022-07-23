class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        
        counter1 = collections.Counter(s1)
        counter2 = collections.Counter(s2[:len(s1)])
        matches = 0
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if counter1[c]==counter2[c]: matches += 1
        if matches==26: return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            counter2[s2[r]] += 1
            if counter1[s2[r]]==counter2[s2[r]]:
                matches += 1
            elif counter1[s2[r]]+1==counter2[s2[r]]:
                matches -= 1
            
            counter2[s2[l]] -= 1
            if counter1[s2[l]]==counter2[s2[l]]:
                matches += 1
            elif counter1[s2[l]]-1==counter2[s2[l]]:
                matches -= 1
            l += 1
            
            if matches==26: return True
        return False
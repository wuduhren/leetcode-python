class Solution(object):
    def reverseVowels(self, s):
        i = 0
        j = len(s)-1
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        s = list(s)
        
        while i<j:
            if s[i] not in vowels:
                i += 1
                continue
            if s[j] not in vowels:
                j -= 1
                continue
            
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        return "".join(s)
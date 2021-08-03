"""
Time: O(N*wl), N is the length of the input string s; wl is the length of each word.
Space: O(N)

For word count wc and word length wl, the string we are looking for will be between i and j (s[i:j]).
`test()` all s[i:j]. If pass, append into ans.

Each `test()` will test the sub-string s[i:j]`.
If any "word" in the sub-string is not in the countExpected, the test failed.
If the word is used too many times (more than "countExpected"), the test failed.
Otherwise, the test pass.

This is the solution I learn from @gabbu.
"""
import collections

class Solution(object):
    def findSubstring(self, s, words):
        if not words: return []
        
        wc = len(words) #word count
        wl = len(words[0]) #word length
        ans = []
        
        i = 0
        j = wc*wl
        
        countExpected = collections.Counter(words)
        
        while j<=len(s):
            if self.test(s[i:j], wl, countExpected): ans.append(i)
            i += 1
            j += 1
        
        return ans
    
    
    def test(self, s, wl, countExpected):
        counter = collections.Counter() #{word:how many time the word is used}
        i = 0
        
        while i<len(s):
            word = s[i:i+wl]
            if word not in countExpected or counter[word]>=countExpected[word]: return False
            i += wl
            counter[word] += 1
            
        return True
        
        
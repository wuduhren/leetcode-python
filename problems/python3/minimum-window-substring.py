class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s): return ""
        
        ans = ""
        counter1 = collections.Counter(t)
        charSet = set(t)
        counter2 = collections.Counter() #sliding window in string s, index between l and r
        charSet2 = set(s)
        matchCount = 0 #count of char in the sliding window that counts are larger than the char count in t.
        
        l = 0
        for r in range(len(s)):
            counter2[s[r]] += 1
            
            if s[r] in charSet and counter1[s[r]]==counter2[s[r]]: matchCount += 1
                
            while l<len(s) and (s[l] not in charSet or counter2[s[l]]>counter1[s[l]]):
                counter2[s[l]] -= 1
                l += 1
                
            if matchCount==len(charSet) and (ans=="" or r-l+1<len(ans)):
                ans = s[l:r+1]
                
        return ans
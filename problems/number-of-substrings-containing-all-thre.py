class Solution(object):
    def numberOfSubstrings(self, s):
        #number of subarrays that at most have k unique char
        def atMost(k):
            counter = collections.Counter()
            uniqueCount = 0
            ans = 0
            i = 0
            
            for j, c in enumerate(s):
                counter[c] += 1
                if counter[c]==1: uniqueCount += 1

                while uniqueCount>k:
                    counter[s[i]] -= 1
                    if counter[s[i]]==0: uniqueCount-= 1
                    i += 1
                ans += j-i+1
            return ans
        
        n = len(s)
        return atMost(3) - atMost(2)
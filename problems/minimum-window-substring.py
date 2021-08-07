"""
Time: O(S+T)
Space: O(S+T)

Moving pointers l and r to change the window.
The window we desired is the one that `actual==required`. (`windowCounter` and `tCounter` help us to track required and actual)
If the window is not what we desired, keep expand right.
If the window is what we desired, contract the window from left, see if we can find shorter ans.
"""
import collections

class Solution(object):
    def minWindow(self, s, t):
        ans = s
        ansFound = False
        windowCounter = collections.Counter()
        tCounter = collections.Counter(t)
        required = len(tCounter) #number of unique char in t
        actual = 0 #number of unique char in t in the window that has the count needed in tCounter
        r = l = 0
        
        while r<len(s):
            cr = s[r] #char right
            windowCounter[cr] += 1
            if cr in tCounter and windowCounter[cr]==tCounter[cr]: actual += 1
            
            #after having the desired window (actual==required)
            #update the ans
            #also start constrating the window from the left
            while l<=r and actual==required:
                if len(s[l:r+1])<=len(ans):
                    ans = s[l:r+1]
                    ansFound = True
                
                cl = s[l]
                windowCounter[cl] -= 1
                if cl in tCounter and windowCounter[cl]<tCounter[cl]: actual -= 1
                l += 1
            
            r += 1
        
        return ans if ansFound else ""
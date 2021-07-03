#https://leetcode.com/problems/backspace-string-compare/
class Solution:
    #Compare from backward. Because we need to count the hashtags first.
    #Compare the char that are not canceled by the hashtags, letter by letter.
    #So we don't have to convert the whole string if they are not the same.
    #Return Fasle, as soon as we find out that they are not the same.
    
    def backspaceCompare(self, S1, S2):
		#index compared so far
        i = len(S1)-1
        j = len(S2)-1
		
        while i>=0 or j>=0:
			#the first char that are not canceled by the hashtags
            c1 = ''
            c2 = ''
            
            if i>=0:
                c1, i = self.getChar(S1, i)
            if j>=0:
                c2, j = self.getChar(S2, j)
            if c1!=c2:
                return False
        return True
    
    def getChar(self, s, i):
		#return the first character that are not canceled by the hashtag
		#return inedx compared so far so we don't have to do that again
        c = ''
        hashtag = 0
        
        while i>=0 and c=='':
            char = s[i]
            if char=='#':
                hashtag+=1
            elif hashtag==0:
                c = char
            else:
                hashtag-=1
            i-=1
        return c, i
"""
Time: O(N)
Space: O(1)
"""
class Solution(object):
    def backspaceCompare(self, s1, s2):
        i = len(s1)-1
        j = len(s2)-1
        c1 = 0 #s1 unprocessed backspace count
        c2 = 0 #s2 unprocessed backspace count
        
        while i>=0 or j>=0:
            while i>=0:
                if s1[i]=='#':
                    c1 += 1
                    i -= 1
                elif c1>0:
                    c1 -= 1
                    i -= 1
                else:
                    break
            
            while j>=0:
                if s2[j]=='#':
                    c2 += 1
                    j -= 1
                elif c2>0:
                    c2 -= 1
                    j -= 1
                else:
                    break
            
            # if one of the string is finished, the other one should be finished, too.
            if i<0: return j<0
            if j<0: return i<0
            
            
            if s1[i]!=s2[j]: return False
            
            i -= 1
            j -= 1
            
        return True
        
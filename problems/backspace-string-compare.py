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
#https://leetcode.com/problems/license-key-formatting/
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        r = ''
        s = S.replace('-', '').upper()
        
        #cut first part of string
        remainder = len(s)%K
        if remainder!=0:
            r = s[:remainder]+'-'
            s = s[remainder:]
        
        while len(s)>0:
            r += s[:K]+'-'
            s = s[K:]
        
        #remove last '-'
        r = r[:-1]
        
        return r
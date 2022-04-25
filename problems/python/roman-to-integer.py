#https://leetcode.com/problems/roman-to-integer/
class Solution(object):
    def romanToInt(self, s):
        counter = 0
        special = {
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900,
        }
        normal = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        for char, num in special.items():
            if char in s:
                counter+=num
                s = s.replace(char, '')
                if s=='':
                    return counter
                
        for char, num in normal.items():
            if char in s:
                counter+=num*s.count(char)
                s = s.replace(char, '')
                if s=='':
                    return counter
                
                
        return counter



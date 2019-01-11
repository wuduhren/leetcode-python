#https://leetcode.com/problems/add-digits/
class Solution(object):
    def addDigits(self, num):
        if num==0: return 0
        
        while len(str(num))>1:
            counter = 0
            for i in str(num):
                counter+=int(i)
            num = counter
        return num
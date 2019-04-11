#https://leetcode.com/problems/add-digits/
class Solution(object):
    def addDigits(self, num):
        if num<10: return num
        total = 0
        while num>9:
            total = 0
            for d in str(num):
                total+=int(d)
            num = total
        return num
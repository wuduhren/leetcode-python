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

"""
I really take time tried to make the best solution or explaination. 
Because I wanted to help others like me. 
If you like my answer, a star on GitHub means a lot to me. 
https://github.com/wuduhren/leetcode-python
"""
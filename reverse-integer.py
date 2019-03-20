#https://leetcode.com/problems/reverse-integer/
class Solution(object):
    def reverse(self, x):
        if x>=(2**31)-1 or x<(-2)**31:
            return 0
        
        if x>=0:
            x = str(x)[::-1]
        else:
            x = str(-x)[::-1]
            x = '-'+x
            
        if x[0] == '0':
            x = x[0:]
            
        x = int(x)
        
        if x>=(2**31)-1 or x<(-2)**31:
            return 0
        
        return x

"""
I really take time to explain my solution, because I wanted to help people understand.
If you like my answer, a star on GitHub I will really appreciated.
https://github.com/wuduhren/leetcode-python
"""
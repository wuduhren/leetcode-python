#https://leetcode.com/problems/add-binary/
class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a, 2)+int(b, 2))[2:]

"""
I really take time to make the best solution, because I wanted to help people understand.
If you like my answer, a star on GitHub I will really appreciated.
https://github.com/wuduhren/leetcode-python
"""
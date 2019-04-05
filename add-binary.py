#https://leetcode.com/problems/add-binary/
class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a, 2)+int(b, 2))[2:]
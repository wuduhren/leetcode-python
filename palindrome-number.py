#https://leetcode.com/problems/palindrome-number/
class Solution(object):
    def isPalindrome(self, x):
        return str(x)==str(x)[::-1]
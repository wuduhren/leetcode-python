#https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        if (s==''):
            return True
        elif ('()' in s):
            return self.isValid(s.replace('()', ''))
        elif ('[]' in s):
            return self.isValid(s.replace('[]', ''))
        elif ('{}' in s):
            return self.isValid(s.replace('{}', ''))
        else:
            return False
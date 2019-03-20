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

"""
I really take time to make the best solution, because I wanted to help people understand.
If you like my answer, a star on GitHub I will really appreciated.
https://github.com/wuduhren/leetcode-python
"""
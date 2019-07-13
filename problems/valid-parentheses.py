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


class Solution(object):
    def isValid(self, s):
        stack = []
        for c in s:
            if c=='(' or c=='[' or c=='{':
                stack.append(c)
            elif c==')':
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(c)
            elif c==']':
                if stack and stack[-1]=='[':
                    stack.pop()
                else:
                    stack.append(c)
            elif c=='}':
                if stack and stack[-1]=='{':
                    stack.pop()
                else:
                    stack.append(c)
        return len(stack)==0
        
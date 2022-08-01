class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', ']': '[', '}':'{'}
        stack = []
        
        for c in s:
            if c not in mapping:
                #open parentheses
                stack.append(c)
            else:
                #close parentheses
                if stack and stack[-1]==mapping[c]:
                    stack.pop()
                else:
                    return False
        
        return not stack
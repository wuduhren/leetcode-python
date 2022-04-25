class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        i = 0
        while i<len(s):
            if stack and stack[-1]==s[i]:
                stack.pop()    
            else:
                stack.append(s[i])
            i += 1
        
        return ''.join(stack)
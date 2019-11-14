#recursion
#the main idea is to only calculate the mosr outer layer. (which is when stack is empty.)
#we put all the inner layer to another `decodeString()` to get its value.
#time: O(N), N is the length of the string.
#space: O(N).
class Solution(object):
    def decodeString(self, s):
        opt = ''
        k = ''
        stack = []

        for i, c in enumerate(s):
            if c=='[':
                stack.append(i)
            elif c==']':
                i_start = stack.pop()
                if not stack:
                    opt += int(k)*self.decodeString(s[i_start+1:i])
                    k = ''
            elif c.isdigit() and not stack:
                k+=c
            elif not stack:
                opt+=c
        return opt or s

#stack
#as we iterate the string, we will dive into different level of brackets.
#we store the value of the current level in the `opt`
#and store the outer level in the stack
#when we get out of this level, we calculate the value.
#time: O(N), N is the length of the string.
#space: O(N).
class Solution(object):
    def decodeString(self, s):
        opt = ''
        stack = []
        k = ''

        for c in s:
            if c=='[':
                stack.append(opt)
                stack.append(k)
                opt = ''
                k = ''
            elif c==']':
                n = stack.pop()
                pre = stack.pop()
                opt = pre+int(n)*opt
            elif c.isdigit():
                k+=c
            else:
                opt+=c
        return opt






class Solution(object):
    def calculate(self, s):
        s += '+' #edge case, for last operation to be executed.
        lastOperation = '+' #edge case, for the first currNum
        operations = set(['+', '-', '*', '/'])
        
        stack = []
        currNum = 0

        for c in s:
            if c.isdigit():
                currNum = currNum*10 + int(c)
            elif c in operations:
                if lastOperation=='+':
                    stack.append(currNum)
                    currNum = 0
                elif lastOperation=='-':
                    stack.append(-currNum)
                    currNum = 0
                elif lastOperation=='*':
                    currNum = stack.pop() * currNum
                    stack.append(currNum)
                    currNum = 0
                elif lastOperation=='/':
                    currNum = stack.pop() / currNum
                    if currNum<0: currNum += 1
                    stack.append(currNum)
                    currNum = 0
                lastOperation = c
        
        return sum(stack)
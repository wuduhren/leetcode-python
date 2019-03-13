"""
iterate through the tokens

if the token is +-*/
then take out two operands to calculate with the operator
put the result to stack
(take 2 operands out bc +-*/ are all binary operator)

if the token is operands
put it to stack

the final answer should be the one left in the stack
"""
class Solution(object):
    def evalRPN(self, tokens):
        def calculate(operator, n1, n2):
            if operator=='+':
                return n2+n1
            elif operator=='-':
                return n2-n1
            elif operator=='*':
                return n2*n1
            elif operator=='/' and n1!=0:
                #by description
                #division between two integers should truncate toward zero.
                if n2%n1!=0:
                    return int(n2/float(n1))
                else:
                    return n2/n1
            else:
                print('ERROR')
                
        stack = []
        
        for t in tokens:
            if t in '+-*/':
                stack.append(calculate(t, stack.pop(), stack.pop()))
            else:
                stack.append(int(t))
        return stack.pop()
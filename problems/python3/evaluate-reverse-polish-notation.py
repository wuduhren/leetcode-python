class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '-', '*', '/'])
        stack = []
        
        for c in tokens:
            if c in operators:
                n2 = stack.pop()
                n1 = stack.pop()
                
                if c=='+':
                    stack.append(n1+n2)
                elif c=='-':
                    stack.append(n1-n2)
                elif c=='*':
                    stack.append(n1*n2)
                elif c=='/':
                    stack.append(int(n1/n2))
            else:
                stack.append(int(c))
        
        return stack.pop()
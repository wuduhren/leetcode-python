class Solution(object):
    def diffWaysToCompute(self, S):
        def calculate(operator, n1, n2):
            if operator=="+":
                return n1+n2
            elif operator=='-':
                return n1-n2
            elif operator=='*':
                return n1*n2
            else:
                return None

        if S.isdigit(): return [int(S)]

        opt = []
        for i in xrange(len(S)):
            if S[i]=='+' or S[i]=='-' or S[i]=='*':
                left = self.diffWaysToCompute(S[:i])
                right = self.diffWaysToCompute(S[i+1:])
                for n1 in left:
                    for n2 in right:
                        opt.append(calculate(S[i], n1, n2))
        return opt

class Solution(object):
    def splitIntoFibonacci(self, S):
        def is_bibonacci(opt, num):
            return num == opt[-1]+opt[-2]

        def helper(s, first):
            if first==len(s) and len(opt)>=3:
                return True

            for i in xrange(first, len(s)):
                if s[first]=='0' and i!=first: break #skip leading zero
                num = int(s[first:i+1])

                if num>2147483648: break

                #early termination
                if len(opt)>=2 and num>opt[-1]+opt[-2]:
                    break

                if len(opt)<=1 or is_bibonacci(opt, num):
                    opt.append(int(num))
                    if helper(s, i+1): return True
                    opt.pop()
            return False

        opt = []
        helper(S, 0)
        return opt







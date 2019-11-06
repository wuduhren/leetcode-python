class Solution(object):
    def splitIntoFibonacci(self, S):
        def findIndex(s, num):
            for i, c in enumerate(num):
                if i>=len(s): break
                if c!=s[i]: break
                if i==len(num)-1: return i+1
            return -1

        def search(fab, s):
            if len(s)==0: return fab
            if len(fab)<2: return []

            target = fab[-1]+fab[-2]
            if target>2147483648: return []
            i = findIndex(s, str(target))
            if i>0: return search(fab+[target], s[i:])
            return []

        for i in xrange(1, len(S)-2):
            for j in xrange(i+1, len(S)-1):
                #skip leading zero
                if (S[:i][0]!='0' and S[:i][0]=='0') or (S[i:j][0]!='0' and S[i:j][0]=='0'): continue
                opt = search([int(S[:i]), int(S[i:j])], S[j:])
                if len(opt)>0: return opt
        return []



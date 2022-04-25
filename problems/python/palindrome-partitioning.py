class Solution(object):
    def partition(self, S):
        def isPalindrome(s):
            return len(s)==1 or (len(s)>0 and s==s[::-1])
        def search(s, pal_list):
            if len(s)==0:
                opt.append(pal_list)
                return
            for i in xrange(1, len(s)+1):
                if isPalindrome(s[:i]):
                    search(s[i:], pal_list+[s[:i]])
        opt = []
        search(S, [])
        return opt
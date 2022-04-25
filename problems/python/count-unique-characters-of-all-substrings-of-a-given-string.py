class Solution(object):
    def uniqueLetterString(self, s):
        index = {}
        ans = 0
        for c in 'abcdefghijklmnopqrstuvwxyz':
            index[c.upper()] = [-1, -1]
        
        # count the substring that s[j] is the unique letter
        for k, c in enumerate(s):
            i, j = index[c]
            ans += (j-i) * (k-j)
            index[c] = [j, k]
        
        # count the substring that s[j] is the unique letter, because last iteration did not count the last letter
        for c in index:
            i, j = index[c]
            ans += (j-i) * (len(s)-j)
        return ans
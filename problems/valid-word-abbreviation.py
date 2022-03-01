class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        #process abbr
        splitedAbbr = []
        for c in abbr:
            if c.isdigit() and splitedAbbr and splitedAbbr[-1][0].isdigit():
                splitedAbbr[-1] += c
            elif c.isdigit() and c=='0':
                return False #leading 0
            else:
                splitedAbbr.append(c)
        for i, c in enumerate(splitedAbbr):
            if c[0].isdigit(): splitedAbbr[i] = int(c)
                    
        i = 0
        j = 0
        while i<len(word) and j<len(splitedAbbr):
            if word[i]==splitedAbbr[j]:
                i += 1
                j += 1
                continue
            
            if isinstance(splitedAbbr[j], basestring):
                return False
            else:
                splitedAbbr[j] -= 1
                if splitedAbbr[j]==0: j += 1
                i += 1
        
        return i==len(word) and j==len(splitedAbbr)
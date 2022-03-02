class Solution(object):
    def isNumber(self, s):
        def isOK(s, maxDots):
            if not s: return False
            
            #check and remove +/-
            for i, c in enumerate(s):
                if (c=='+' or c=='-') and i!=0:
                    return False
            if s[0]=='+' or s[0]=='-': s = s[1:]
            
            #check dot and if there is digit
            dotCount = 0
            dotPos = 0
            digitCount = 0
            for i, c in enumerate(s):
                if c=='.':
                    dotCount += 1
                    dotPos = i
                elif c.isdigit():
                    digitCount += 1
            
            if dotCount>maxDots: return False
            if digitCount==0: return False
            
            return True
        
        #get e's position. Also check if all char is in validChar
        validChar = set(['1','2', '3', '4', '5', '6', '7', '8', '9', '0', 'e', 'E', '.', '+', '-'])
        eCount = 0
        ePos = 0
        for i, c in enumerate(s):
            if c not in validChar:
                return False
            if c=='e' or c=='E':
                eCount += 1
                ePos = i
            
        if eCount>1:
            return False
        elif eCount==1:
            return isOK(s[:ePos], 1) and isOK(s[ePos+1:], 0)
        else:
            return isOK(s, 1)

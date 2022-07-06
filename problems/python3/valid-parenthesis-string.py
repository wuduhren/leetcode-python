class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = 0
        leftMax = 0
        
        for c in s:
            if c=='(':
                leftMin += 1
                leftMax += 1
            elif c==')':
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            
            if leftMax<0:
                return False
            
            if leftMin<0:
                leftMin = 0
        
        return leftMin == 0
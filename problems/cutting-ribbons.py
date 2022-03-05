class Solution(object):
    def maxLength(self, ribbons, k):
        maxLen = max(ribbons)
        minLen = 0
        
        while minLen<maxLen:
            l = minLen + (maxLen-minLen+1)/2
            
            if sum([ribbonLen/l for ribbonLen in ribbons])>=k:
                minLen = l
            else:
                maxLen = l-1
        return maxLen
class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        compare a[i] and b[j]
        if a[i]!=b[j], return -1 
        if a new set of "a" is needed, count += 1
        """
        def helper(i):
            count = 1
            j = 0
            
            while j<len(b):
                if a[i]!=b[j]: return -1
                j += 1
                
                if i==len(a)-1 and j<len(b):
                    # if we need an extra "a", count += 1
                    i = 0
                    count += 1
                else:
                    i += 1
            return count
        
        if len(set(b)-set(a))>0: return -1
        
        #the index of the starting point need to be as small as posible. So that we can get the minimum answer.
        for i in xrange(len(a)):
            if a[i]==b[0]:
                ans = helper(i)
                if ans>0: return ans
        
        return -1
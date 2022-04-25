class SummaryRanges(object):

    def __init__(self):
        self.nums = []
        

    def addNum(self, val):
        bisect.insort_left(self.nums, val)
        

    def getIntervals(self):
        ans = []
        
        for num in self.nums:
            if not ans:
                ans.append([num, num])
            elif ans[len(ans)-1][1]+1==num:
                ans[len(ans)-1][1] = num
            elif ans[len(ans)-1][1]<num:
                ans.append([num, num])
        return ans


"""
addNum() Time: O(N), Though finding the insertion point only takes O(LogN), insert to array still takes O(N).
getIntervals() Time: O(1)
Space: O(1)
"""
class SummaryRanges(object):

    def __init__(self):
        self.ans = []
    
    def addNum(self, val):
        if not self.ans:
            self.ans.append([val, val])
            return
            
        l = 0
        r = len(self.ans)-1
        
        #find insertion point
        while l<r:
            m = (l+r)/2
            if self.checkAndAdd(l, val): return
            if self.checkAndAdd(r, val): return
            if self.checkAndAdd(m, val): return
            
            if val<self.ans[m][0]:
                r = m
            else:
                l = m+1
        
        #insert val
        if self.checkAndAdd(l, val):
            return
        elif val<self.ans[l][0]:
            self.ans.insert(l, [val, val])
        else:
            self.ans.insert(l+1, [val, val])
        
    def getIntervals(self):
        return self.ans
    
    #add if val can add to self.ans[i]
    def checkAndAdd(self, i, val):
        if val==self.ans[i][0]-1:
            self.ans[i][0] = val

            #merge i-1 and i if needed
            if i>0 and self.ans[i-1][1]+1==self.ans[i][0]:
                self.ans[i][0] = self.ans[i-1][0]
                self.ans.pop(i-1)

            return True

        elif val==self.ans[i][1]+1:
            self.ans[i][1] = val

            #merge i and i+1 if needed
            if i+1<len(self.ans) and self.ans[i][1]+1==self.ans[i+1][0]:
                self.ans[i][1] = self.ans[i+1][1]
                self.ans.pop(i+1)

            return True

        elif self.ans[i][0]<=val and val<=self.ans[i][1]:
            return True

        return False
        
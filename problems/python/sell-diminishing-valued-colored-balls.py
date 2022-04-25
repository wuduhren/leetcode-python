class Solution(object):
    def maxProfit(self, I, orders):
        I.sort(reverse=True)
        I.append(0)
        
        profit = 0
        w = 1
        
        for i in xrange(len(I)-1):
            if orders==0: break
            if I[i]>I[i+1]:
                if w*(I[i]-I[i+1])<orders:
                    profit += w*self.sumRange(I[i+1]+1, I[i])
                    orders -= w*(I[i]-I[i+1])
                else:
                    h, remain = divmod(orders, w)
                    profit += w*self.sumRange(I[i]-h+1, I[i])
                    profit += remain*(I[i]-h)
                    orders -= w*h+remain
            w += 1
        
        return profit % (10**9+7)
    
    def sumRange(self, low, high):
        return (high+low)*(high-low+1)/2
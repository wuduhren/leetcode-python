class Solution(object):
    def candy(self, ratings):
        N = len(ratings)
        
        l2r = [1]*N
        r2l = [1]*N
        
        for i in xrange(1, N):
            if ratings[i]>ratings[i-1]:
                l2r[i] = l2r[i-1]+1
        
        for i in xrange(N-2, -1, -1):
            if ratings[i]>ratings[i+1]:
                r2l[i] = r2l[i+1]+1
        
        ans = 0
        for i in xrange(N):
            ans += max(l2r[i], r2l[i])
        
        return ans
        
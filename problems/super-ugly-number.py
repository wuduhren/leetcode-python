class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        p = [0]*len(primes) #p[i] stores the index of ugly number in ans that not yet times primes[i] yet
        ans = [1]
        h = []
        
        for i in xrange(len(primes)):
            heapq.heappush(h, (primes[i]*ans[p[i]], i))
            
        for _ in xrange(n-1):
            curr = h[0][0]
            ans.append(curr)
            
            while h and h[0][0]==curr:
                i = h[0][1]
                heapq.heappop(h)
                p[i] += 1
                heapq.heappush(h, (primes[i]*ans[p[i]], i))
        
        return ans[-1]
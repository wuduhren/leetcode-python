class Solution(object):
    def numTilings(self, N):
        H = [[0, 0] for _ in xrange(N+1)]
        H[0][0] = 1
        H[1][0] = 1
        
        for i in xrange(2, N+1):
            H[i][0] = (H[i-1][0] + H[i-2][0] + H[i-1][1]*2) % 1000000007
            H[i][1] = (H[i-2][0] + H[i-1][1]) % 1000000007
            
        return H[N][0]
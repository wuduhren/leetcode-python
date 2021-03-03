"""
dp[i] := min height when storing books 0~i
for each j try to add a new line at i, see the min height.

Time: O(N^2)
Space: O(N)
"""
class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        N = len(books)
        dp = [float('inf')]*N
        
        for j in xrange(N):
            w = 0
            h = 0
            for i in xrange(j, -1, -1):
                w+=books[i][0]
                if w>shelf_width: break
                
                h = max(h, books[i][1])
                if i==0:
                    dp[j] = min(dp[j], h)
                else:
                    dp[j] = min(dp[j], dp[i-1]+h)
        return dp[-1]
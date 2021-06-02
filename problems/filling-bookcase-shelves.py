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


"""
dp[i] := smallest height that the last book on book shelve is books[i]
dp[i] = min { dp[j]+max(books[j+1:i]) where sumWidth(books[j+1:i])<=W, j = 0~i-1}
"""
class Solution(object):
    def minHeightShelves(self, books, W):
        dp = [float('inf')]*len(books)
        
        dp[0] = books[0][1]
        
        for i in xrange(1, len(books)):
            topLevelWidth = 0
            topLevelMaxHeight = 0
            
            for j in xrange(i, -1, -1):
                topLevelWidth += books[j][0]
                topLevelMaxHeight = max(topLevelMaxHeight, books[j][1])
                if topLevelWidth>W: break
                dp[i] = min(dp[i], (dp[j-1] if j-1>=0 else 0) + topLevelMaxHeight)
                
        return dp[-1]
                
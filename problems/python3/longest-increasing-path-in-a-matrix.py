"""
Time: O(MN) since the memo at most has MN index.
Space: O(MN)
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i0, j0):
            if (i0, j0) in memo: return memo[(i0, j0)]
            ans = 1
            
            for i, j in ((i0+1, j0), (i0-1, j0), (i0, j0+1),(i0, j0-1)):
                if i<0 or i>=N or j<0 or j>=M: continue
                if matrix[i][j]<=matrix[i0][j0]: continue
                ans = max(ans, 1+dfs(i, j))
            
            memo[(i0, j0)] = ans
            return ans
            
        N = len(matrix)
        M = len(matrix[0])
        memo = {}
        ans = 0
        for i in range(N):
            for j in range(M):
                ans = max(ans, dfs(i, j))
        return ans
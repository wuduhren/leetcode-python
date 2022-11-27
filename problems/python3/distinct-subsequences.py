class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def dfs(i, j):
            if (i, j) in visited: return visited[(i, j)]
            
            if j>=len(t): return 1
            if i>=len(s): return 0
            
            if s[i]==t[j]:
                visited[(i, j)] = dfs(i+1, j+1)+dfs(i+1, j)
            else:
                visited[(i, j)] = dfs(i+1, j)
            return visited[(i, j)]
            
        visited = {}
        dfs(0, 0)
        return dfs(0, 0)
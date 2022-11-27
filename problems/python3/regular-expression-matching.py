class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(i, j):
            if (i, j) in cache: return cache[(i, j)]
            if i>=M and j>=N: return True
            if j>=N: return False
            
            match = i<M and (s[i]==p[j] or p[j]=='.')
            
            if j+1<N and p[j+1]=='*':
                cache[(i, j)] = (match and dfs(i+1, j)) or dfs(i, j+2) #(use one or more p[j]) or (use zero p[j])
                return cache[(i, j)]
            
            if match:
                cache[(i, j)] = dfs(i+1, j+1)
                return cache[(i, j)]
            
            cache[(i, j)] = False
            return cache[(i, j)]
        
        cache = {}
        M = len(s)
        N = len(p)
        return dfs(0, 0)
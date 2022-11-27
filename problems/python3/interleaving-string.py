class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def dfs(i, j):
            if (i, j) in history: return False
            if i+j==len(s3): return True
            if i<len(s1) and s3[i+j]==s1[i] and dfs(i+1, j): return True
            if j<len(s2) and s3[i+j]==s2[j] and dfs(i, j+1): return True
            history.add((i, j))
            return False
        
        if len(s1)+len(s2)!=len(s3): return False
        history = set() #store the failed cases
        return dfs(0, 0)
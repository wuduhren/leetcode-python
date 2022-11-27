"""
dfs(i, j)
i being the unprocessed index in word1.
j, word2.

MAIN LOGIC:
if word1[i]==word2[j], no operation need, return dfs(i+1, j+1)
if not, need 1 operation, so
replace: dfs(i+1, j+1)
insert: dfs(i, j+1)
delete: dfs(i+1, j)

BASE CASE:
If both string are empty (i==N and j==M), no operation needed.
If one string are empty, then the remain operation is the length of the non-empty one.
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)
        def dfs(i, j)->int:
            if i==N and j==M: return 0
            if i==N: return M-j
            if j==M: return N-i
            
            if (i, j) in history:
                return history[(i, j)]
                
            if word1[i]==word2[j]:
                history[(i, j)] = dfs(i+1, j+1)
            else:
                history[(i, j)] = 1+min(dfs(i+1, j+1), dfs(i+1, j), dfs(i, j+1))
            
            return history[(i, j)]
        
        history = {}
        return dfs(0, 0)
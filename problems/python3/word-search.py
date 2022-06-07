class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(x, i, j):
            if i<0 or i>=N or j<0 or j>=M: return False
            if (i, j) in usedWords: return False
            usedWords.add((i, j))
            
            if word[x]==board[i][j]:
                if x==len(word)-1:
                    return True
                else:
                    if helper(x+1, i+1, j): return True
                    if helper(x+1, i, j+1): return True
                    if helper(x+1, i-1, j): return True
                    if helper(x+1, i, j-1): return True
                    
                    
            usedWords.remove((i, j))
            return False
                    
        usedWords = set()
        N = len(board)
        M = len(board[0])
        for i in range(N):
            for j in range(M):
                if helper(0, i, j): return True
        return False
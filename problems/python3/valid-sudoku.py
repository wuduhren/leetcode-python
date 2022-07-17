class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def rowIsValid(i):
            used = set()
            for j in range(N):
                if board[i][j]=='.': continue
                if board[i][j] in used: return False
                used.add(board[i][j])
            return True
        
        def columnIsValid(i):
            used = set()
            for j in range(N):
                if board[j][i]=='.': continue
                if board[j][i] in used: return False
                used.add(board[j][i])
            return True
        
        def isBoxValid(i1, i2, j1, j2):
            used = set()
            for i in range(i1, i2+1):
                for j in range(j1, j2+1):
                    if board[i][j]=='.': continue
                    if board[i][j] in used: return False
                    used.add(board[i][j])
            return True
                
        N = 9
        for i in range(N):
            if not rowIsValid(i): return False
            if not columnIsValid(i): return False
        
        for i in range(0, N, 3):
            for j in range(0, N, 3):
                if not isBoxValid(i, i+2, j, j+2): return False
        
        return True
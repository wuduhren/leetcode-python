"""
Time: O(N)
Space: O(N)
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i0, j0):
            if i0<0 or j0<0 or i0>=MAX_ROW or j0>=MAX_COL: return
            if board[i0][j0]!='O': return
            if (i0, j0) in survived: return
            
            survived.add((i0, j0))
            dfs(i0+1, j0)
            dfs(i0-1, j0)
            dfs(i0, j0+1)
            dfs(i0, j0-1)
        
        
        MAX_ROW = len(board)
        MAX_COL = len(board[0])
        survived = set()
        
        for i in range(MAX_ROW):
            dfs(i, 0)
            dfs(i, MAX_COL-1)
        
        for j in range(MAX_COL):
            dfs(0, j)
            dfs(MAX_ROW-1, j)
        
        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                board[i][j] = 'O' if (i, j) in survived else 'X'
        return board